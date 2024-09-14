from sentence_transformers import SentenceTransformer
from db import SessionLocal, Document
import numpy as np
from scipy.spatial.distance import cosine


model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def perform_search(text, top_k=5, threshold=0.5):
    query_embedding = model.encode(text).tolist()

    
    db_session = SessionLocal()
    documents = db_session.query(Document).all()
    db_session.close()

    results = []
    for doc in documents:
        similarity = 1 - cosine(query_embedding, doc.document_embedding)
        if similarity >= threshold:
            results.append((doc.doc_id, similarity, doc.document_text))

    
    results.sort(key=lambda x: x[1], reverse=True)
    return results[:top_k]
