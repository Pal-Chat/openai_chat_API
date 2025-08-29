from app.vector_search import index, documents
from app.embeddings import embed_text
import numpy as np
import openai

async def generate_response(context: str, query: str) -> str:
    """
    Generate a chat response from OpenAI's model using provided context.

    Steps:
    - Create a prompt combining the matched document (context) and the user's query.
    - Call OpenAI's ChatCompletion API asynchronously with the prompt.
    - Extract and return the assistant's reply text from the API response.

    Args:
        context (str): The related document text found by vector search.
        query (str): The user's input question or message.

    Returns:
        str: The AI-generated response based on input context and query.
    """
    # Format prompt to include context and user query for better AI understanding
    prompt = f"Context: {context}\nUser: {query}\nAssistant:"

    # Make asynchronous call to OpenAI chat completion endpoint with the prompt
    response = await openai.ChatCompletion.acreate(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": prompt}],
    )
    # Return the content of the generated assistant message
    return response['choices'][0]['message']['content']

async def find_most_similar_document(query: str) -> str:
    """
    Find the document most relevant to the user query using vector similarity.

    Steps:
    - Embed the user query into a numeric vector using OpenAI embeddings.
    - Convert the embedding into a NumPy array of the correct type/shape for FAISS.
    - Search the FAISS index to identify the nearest (most similar) document vector.
    - Retrieve and return the matching document text.

    Args:
        query (str): The user's input query string.

    Returns:
        str: The text of the most similar document to the query.
    """
    # Generate embedding vector for the user query
    query_embedding = await embed_text(query)

    # Convert embedding list to 2D float32 NumPy array required by FAISS
    xq = np.array(query_embedding).astype('float32').reshape(1, -1)

    # Search FAISS index - get top 1 closest document (distance D, index I)
    D, I = index.search(xq, k=1)

    # Retrieve the text of the document corresponding to the closest index
    matched_doc = documents[I[0][0]]
    return matched_doc
