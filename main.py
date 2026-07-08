import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

with open("data.txt", "r") as file:
    data = file.read()

question = input("Whats your question: ")
prompt = data + question

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=prompt
)

print(interaction.output_text)