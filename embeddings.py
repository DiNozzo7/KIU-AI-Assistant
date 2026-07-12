import os
from dotenv import load_dotenv
from google import genai
import json

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def gen_embeddings(data: list[str]) -> dict:
    dict_of_data = {}
    for doc in data:
        with open(f"data/{doc}", "r") as f:
            doc_bytes = f.read()

        result = client.models.embed_content(
                model="gemini-embedding-2",
                contents=doc_bytes)
        dict_of_data[doc] = result.embeddings[0].values
    return dict_of_data

def save_embeddings(dict_of_data: dict) -> None:
    with open("embeddings.json", "w") as f:
        json.dump(dict_of_data, f, indent=4)
