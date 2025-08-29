from app.vector_search import index, documents
from app.embeddings import embed_text
import numpy as np
import openai

async def generate_response(context: str, query: str) -> str:
    """
    Generate chat response using OpenAI completion.
    The context comes from vector search matched document.
    """
    prompt = f"Context: {context}\nUser: {query}\nAssistant:"
    response = await openai.ChatCompletion.acreate(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": prompt}],
    )
    return response['choices'][0]['message']['content']

async def find_most_similar_document(query: str) -> str:
    """
    Embed user query and find most similar document from index.
    """
    query_embedding = await embed_text(query)
    xq = np.array(query_embedding).astype('float32').reshape(1, -1)
    D, I = index.search(xq, k=1)
    matched_doc = documents[I[0][0]]
    return matched_doc
