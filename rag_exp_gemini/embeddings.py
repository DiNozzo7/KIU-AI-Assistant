import os
from dotenv import load_dotenv
from google import genai
import numpy as np

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
# load api key from .env

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def embedding_list(lst: list):
    embeddings = []

    for text in lst:
        result = client.models.embed_content(
            model="gemini-embedding-2",
            contents=text
        )

        embeddings.append(result.embeddings[0].values)

    return embeddings

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

for embedding in embeddings:
    score = cosine_similarity(comp, embedding)
    scores.append(score)

print(scores)