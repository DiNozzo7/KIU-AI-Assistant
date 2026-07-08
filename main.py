import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

with open("data.txt", "r") as file: # reads data.txt (kiu data)
    data = file.read()

header = '''You are a Kutaisi International University assistant.

Your purpose is to help KIU students and newcomers by answering questions using only the provided university information.

Rules:
- Use the provided information as your main source.
- If the answer is not available in the provided information, clearly say that you do not have this information.
- Do not invent facts.
- Give clear and helpful answers.

Provided information:\n'''
tail = "\nAnswer the user's question:\n"
question = input("Whats your question: ")

prompt = header + data + tail + question # final prompt

interaction = client.interactions.create(
    model="gemini-2.5-flash",
    input=prompt
)

print(interaction.output_text)