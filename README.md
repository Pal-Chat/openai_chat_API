## Overview
This project provides a FastAPI web application that integrates OpenAI's GPT-4 model with semantic vector search (FAISS) and an async SQLAlchemy database. It supports storing users and messages, searching related documents by vector similarity, and generating AI responses with contextual awareness.

## Setup
1. Clone the repo:
git clone <repo-url>
cd my_chat_app

2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

4. Set environment variables in `.env` file:
OPENAI_API_KEY=use_your_openai_API_key
DATABASE_URL=sqlite+aiosqlite:///./test.db

## Running
Start the FastAPI app with:   uvicorn app.main:app --reload
The API will be available at [http://127.0.0.1:8000/docs].

## API Usage

- POST `/chat` with JSON body:
{
"username": "alice",
"query": "Tell me about SQLAlchemy async ORM?"
}

- Response contains AI-generated answer with context from vector search.

## Project Structure

- `app/` - Application code (models, chat logic, vector search)
- `.env` - Environment variables
- `requirements.txt` - Python dependencies
- `documents.txt` - Sample documents for vector indexing
