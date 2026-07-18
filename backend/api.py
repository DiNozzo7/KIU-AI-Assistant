from fastapi import FastAPI
from pydantic import BaseModel
from retrieve import retrieve_similar
from llm import get_information
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    question: str

@app.post("/ask")
def user_question(question: Question):
    question = question.question
    (most_similar, score) = retrieve_similar(question, "embeddings.json")
    answer_of_ai = get_information(question, most_similar)
    return {
        "answer": answer_of_ai,
        "top_score": score
    }