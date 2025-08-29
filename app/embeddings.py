import openai
from typing import List
from app.config import OPENAI_API_KEY

# Set OpenAI API key
openai.api_key = OPENAI_API_KEY

def embed_text_sync(text: str) -> List[float]:
    """Synchronously create text embedding for given text."""
    response = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=text
    )
    return response['data'][0]['embedding']

async def embed_text(text: str) -> List[float]:
    """Asynchronously create text embedding."""
    response = await openai.Embedding.acreate(
        model="text-embedding-ada-002",
        input=text
    )
    return response['data'][0]['embedding']
