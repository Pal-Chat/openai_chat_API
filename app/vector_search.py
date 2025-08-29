import faiss
import numpy as np
from app.embeddings import embed_text_sync

# Dimension of embeddings from text-embedding-ada-002
EMBEDDING_DIM = 1536

# Initialize FAISS index (L2 distance)
index = faiss.IndexFlatL2(EMBEDDING_DIM)

# Sample documents to index
documents = [
    "Hello, this is a test document.",
    "FAISS vector search example.",
    "FastAPI integration with vector search and database.",
    "Async SQLAlchemy ORM usage in Python.",
    "OpenAI API integration demo."
]

document_embeddings = []

def prepare_index():
    """
    Prepare the FAISS index with document embeddings.
    To be called on app startup once.
    """
    global document_embeddings
    document_embeddings = []

    for doc in documents:
        emb = embed_text_sync(doc)
        document_embeddings.append(emb)

    # Convert list to numpy array of float32 for FAISS
    xb = np.array(document_embeddings).astype('float32')

    index.reset()
    index.add(xb)
