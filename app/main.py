from fastapi import FastAPI, HTTPException
from sqlalchemy.future import select
from app.db import async_session, engine, Base
from app.models import User, Message
from app.schemas import ChatRequest, ChatResponse
from app.vector_search import prepare_index
from app.chat import generate_response, find_most_similar_document

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    # Create DB tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Prepare and index document embeddings with FAISS
    prepare_index()

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(chat_request: ChatRequest):
    async with async_session() as session:
        # Check if user exists
        result = await session.execute(select(User).where(User.username == chat_request.username))
        user = result.scalars().first()

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

    return ChatResponse(response=response_text)
