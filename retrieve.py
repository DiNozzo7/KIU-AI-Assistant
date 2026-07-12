import os
from dotenv import load_dotenv
from google import genai
import numpy as np
import json

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def retrieve_similar(question: str, json_file: str) -> list:
    result = client.models.embed_content(
                model="gemini-embedding-2",
                contents=question
                )
    result = result.embeddings[0].values

    with open(json_file, "r") as f:
        data = json.load(f)

    scores = {}
    for key, value in data.items():
        scores[key] = cosine_similarity(result, value)
    
    sorted_scores = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
    return list(sorted_scores.keys())[:2]
