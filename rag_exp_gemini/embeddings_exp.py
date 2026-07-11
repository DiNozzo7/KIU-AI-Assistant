import os
from dotenv import load_dotenv
from google import genai
import numpy as np

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
# load api key from .env

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
# checks similarities


def embedding_list(lst: list):
    embeddings = []

    for text in lst:
        result = client.models.embed_content(
            model="gemini-embedding-2",
            contents=text
        )
        embeddings.append(result.embeddings[0].values)

    return embeddings
# turns the documents into embedding list


documents = [
    "KIU has modern dormitories for students.",
    "KIU offers a Computer Science bachelor's program.",
    "The university is located in Kutaisi."
]

embeddings = embedding_list(documents)


question = input("Whats your question: ")

result = client.models.embed_content(
            model="gemini-embedding-2",
            contents=question
        )

comp = result.embeddings[0].values

scores = []

for document, embedding in zip(documents, embeddings):
    score = cosine_similarity(comp, embedding)
    scores.append((document, score))

scores = sorted(scores, key=lambda x: x[1], reverse=True)


interaction = client.interactions.create(
    model="gemini-2.5-flash",
    input=scores[0][0] + "\nQuestion: " + question
)
print(interaction.output_text)
