import os
from dotenv import load_dotenv
from google import genai
from embeddings import gen_embeddings, save_embeddings
from retrieve import retrieve_similar
from llm import get_information

question = input("Ask a question: ")

data = gen_embeddings(["contacts.txt", "dorms.txt", "programs.txt", "terminology.txt", "transport.txt"])
save_embeddings(data)

most_similar = retrieve_similar(question, "embeddings.json")

answer_of_ai = get_information(question, most_similar)

print(answer_of_ai)