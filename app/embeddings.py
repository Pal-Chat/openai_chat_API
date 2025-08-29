import openai
from typing import List
from app.config import OPENAI_API_KEY

# Configure the OpenAI library with the API key loaded from environment variables.
# This key allows authentication to OpenAI services.
openai.api_key = OPENAI_API_KEY

def embed_text_sync(text: str) -> List[float]:
    """
    Generate an embedding vector for the given text synchronously.

    Steps:
    - Call OpenAI's Embedding API with the text input.
    - Extract the embedding vector from the response.
    
    Args:
        text (str): The input text to embed.

    Returns:
        List[float]: A list of floats representing the text embedding.
    """
    # Synchronous call to OpenAI embedding endpoint (used during startup or blocking code)
    response = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=text
    )
    return response['data'][0]['embedding']

async def embed_text(text: str) -> List[float]:
    """
    Generate an embedding vector for the given text asynchronously.

    Steps:
    - Make an async request to OpenAI's Embedding API.
    - Extract and return the embedding vector.
    
    Args:
        text (str): The input text to embed.

    Returns:
        List[float]: Embedding vector as a float list.
    """
    # Async call enabling non-blocking embeddings during runtime requests
    response = await openai.Embedding.acreate(
        model="text-embedding-ada-002",
        input=text
    )
    return response['data'][0]['embedding']
