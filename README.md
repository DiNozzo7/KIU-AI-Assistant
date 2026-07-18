# KIU (University) AI Assistant

AI assistant to help KIU students or those interested in KIU find important information with just one question.

Live Demo: https://kiu-ai-assistant.vercel.app/

## About The Project

This is my first major personal project that I built by myself within 1 week.

When I first joined university, I had many questions about dormitories, the CS program, and etc. All the questions I had were either unanswered or very hard to find online. In addition, I was "afraid" to ask others for help.

So, a year later, I decided to solve the problem I personally encountered a year ago. During this one year, I encountered many students who were asking questions in university group chats. Many of them remained unanswered, so I tried to gather those questions and add them to my data.

The goal of this project was simple:
**Make university information easier to access through an AI-powered assistant.**

All the information I used as data is public information collected from KIU sources and personal experience.

---

## Features

- AI-powered Q&A system
- RAG approach
- Embeddings
- Custom university data
- FastAPI backend API
- Simple frontend
- Deployed frontend and backend

---

## How It Works

The project uses a RAG pipeline:

1. Custom university data is stored inside the `data/` folder.
2. Each file is converted into embeddings using Gemini embedding models.
3. When a user asks a question:
   - The question is converted into an embedding with the Gemini embedding model.
   - The system finds the most relevant information in `data/` using cosine similarity.
   - The retrieved information is sent to Gemini with additional prompt engineering to generate the final answer.
4. The answer is returned through a FastAPI backend and displayed on the website.

---

## What I Learned

To begin with, I learned how it feels to work on a real project, which I really enjoyed.

Secondly, I reassured myself that the field I am studying is exactly for me because the joy I had during this project was unexplainable.

During development, I learned how RAG works, how embeddings represent text as vectors, and much more. However, the most important thing for me was that I took my first step toward the goal I have.

---

## Final Thoughts

This project started from a personal problem I experienced as a student.

I wanted to create something useful for people who were in the same position I was a year ago; having questions but not knowing where to find answers.

Although this is my first major project, it taught me more than any tutorial could. Building something from an idea, solving problems along the way, and deploying a working product gave me valuable experience that I will continue improving in future projects.
