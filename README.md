# Chat API with Vector Search and OpenAI

## What is this?

This project is a web app that lets users chat with an AI assistant. The AI uses smart search to find helpful information before answering. It stores users and their messages in a database and uses OpenAI’s language model to generate answers.

## How does it work?

- There are some example documents saved in the app.
- When you ask a question, the app turns your words into numbers (called embeddings).
- It compares these numbers with the saved documents to find the most related one.
- The chosen document is sent with your question to OpenAI’s AI model.
- The AI reads the document and then replies to you, making the answer focused and helpful.
- Your messages and username are saved in the database.

## Setup
1. Clone the repo:
git clone <repo-url>
cd my_chat_app

2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate

# On Windows use 
venv\Scripts\activate

4. Install dependencies:
pip install -r requirements.txt

5. Set environment variables in `.env` file:
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

- You will get an AI-generated response based on your query and related documents.

## Why this approach?

This method helps the AI understand your question better by giving it related information to think about. It makes answers more accurate and useful. The database keeps track of who asked what so it can be improved later.


## Project Structure

- `app/` - Application code (models, chat logic, vector search)
- `.env` - Environment variables
- `requirements.txt` - Python dependencies
- `documents.txt` - Sample documents for vector indexing
