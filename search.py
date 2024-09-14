import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from db import SessionLocal, Document


model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def perform_search(text, top_k, threshold):
    """
    Performing search by fetching documents from the database,
    computing cosine similarity with the query embedding,
    and returning the top_k results above the threshold.
    """
    
    query_embedding = model.encode([text])

    
    db_session = SessionLocal()
    documents = db_session.query(Document).all()

    
    document_texts = [doc.document_text for doc in documents]
    document_embeddings = np.array([np.array(doc.document_embedding) for doc in documents])

    # cosine similarity between the query embedding and document embeddings
    similarities = cosine_similarity(query_embedding, document_embeddings)[0]

    # Filtering and sorting results based on threshold and similarity scores
    filtered_results = [
        (doc_text, similarity) for doc_text, similarity in zip(document_texts, similarities)
        if similarity >= threshold
    ]
    filtered_results.sort(key=lambda x: x[1], reverse=True)
    top_results = filtered_results[:top_k]

    db_session.close()
    return [{"document_text": doc_text, "similarity": sim} for doc_text, sim in top_results]
