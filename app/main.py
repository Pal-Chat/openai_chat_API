from fastapi import FastAPI, HTTPException
from sqlalchemy.future import select
from app.db import async_session, engine, Base
from app.models import User, Message
from app.schemas import ChatRequest, ChatResponse
from app.vector_search import prepare_index
from app.chat import generate_response, find_most_similar_document

# Create a FastAPI instance - this is the main app object for routing and config
app = FastAPI()

@app.on_event("startup")
async def startup_event():
    """
    Runs when the application starts.
    - Creates all database tables asynchronously.
    - Prepares and indexes document embeddings using FAISS for vector search.
    This ensures DB and search index are ready before serving requests.
    """
    # Create database tables if they don't exist
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Prepare and index document embeddings with FAISS
    prepare_index()

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(chat_request: ChatRequest):
    """
    API endpoint to handle incoming chat requests.

    Workflow:
    1. Check if the username exists in the database; create if new.
    2. Find the most relevant stored document using vector similarity to the query.
    3. Save the user's query/message in the database.
    4. Generate an AI response using OpenAI's model with matched document context.
    5. Return the AI-generated response to the client.

    Args:
        chat_request (ChatRequest): Incoming JSON payload with username and query.

    Returns:
        ChatResponse: JSON response containing AI-generated reply.
    """
    async with async_session() as session:
        # Check if user exists
        result = await session.execute(select(User).where(User.username == chat_request.username))
        user = result.scalars().first()

        # If user does not exist, add new user to the database
        if not user:
            user = User(username=chat_request.username)
            session.add(user)
            await session.commit()
            await session.refresh(user)

        # Find matching document via vector search
        matched_doc = await find_most_similar_document(chat_request.query)

        # Save message query to DB
        message = Message(user_id=user.id, content=chat_request.query)
        session.add(message)
        await session.commit()

    # Generate response with OpenAI completion using context
    response_text = await generate_response(matched_doc, chat_request.query)

    # Return the AI-generated response in the API response model
    return ChatResponse(response=response_text)
