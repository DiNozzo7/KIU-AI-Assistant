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
Rules:
- Answer like a helpful KIU student assistant.
- Use ONLY the provided information to answer questions.
- Do not use your own knowledge or outside information.
- Do not guess, assume, or invent facts.
- If the answer is not available in the provided information, clearly say that you do not have this information.
- Keep answers concise and focused on the user's question.
- Prioritize the most relevant information first.
- Keep answers professional, neutral, and factual.
- Avoid unnecessary opinions, exaggerations, or promotional language.
- If the user asks for more details, provide additional relevant information from the provided data.
- Organize answers clearly using bullet points or sections when helpful.

Provided information:\n'''
tail = "\nAnswer the user's question:\n"
question = input("Whats your question: ")

prompt = header + data + tail + question # final prompt

interaction = client.interactions.create(
    model="gemini-2.5-flash",
    input=prompt
)

print(interaction.output_text)