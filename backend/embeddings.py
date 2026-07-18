import os
from dotenv import load_dotenv
from google import genai
import json

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# data we want to embed. the files that we want to use as a source of information.
def gen_embeddings(data: list[str]) -> dict:
    """
    input should be the list of .txt files we want to use as a source of information

    outputs the dict of file_name: embedding values
    """
    dict_of_data = {}
    for doc in data:
        with open(f"data/{doc}", "r") as f:
            doc_bytes = f.read()

        result = client.models.embed_content(
                model="gemini-embedding-2",
                contents=doc_bytes)
        dict_of_data[doc] = result.embeddings[0].values
    return dict_of_data

# saves the embedded data into json file
def save_embeddings(dict_of_data: dict) -> None:
    """
    input should be the dict (retreived from gen_embeddings()), where key is file name and value is that file's imbedding

    data is stored in embeddings.json
    """
    with open("embeddings.json", "w") as f:
        json.dump(dict_of_data, f, indent=4)
