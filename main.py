from retrieve import retrieve_similar
from llm import get_information

question = input("Ask a question: ")

most_similar = retrieve_similar(question, "embeddings.json")

answer_of_ai = get_information(question, most_similar)

print(answer_of_ai)