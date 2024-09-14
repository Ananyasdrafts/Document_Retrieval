
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
from db import get_documents

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def perform_search(text, top_k, threshold):
    """
    Performing a search to find top_k most similar documents to the query text.
    """
    query_embedding = model.encode(text)
    
   
    documents = get_documents()  

    if not documents:
        return []

    
    doc_ids, doc_texts, doc_embeddings = zip(*documents)
    doc_embeddings = np.array(doc_embeddings)
    
    
    similarities = cosine_similarity([query_embedding], doc_embeddings)[0]
    
    # Filtering and sorting documents by similarity
    filtered_docs = [(doc_ids[i], doc_texts[i], similarities[i]) for i in range(len(similarities)) if similarities[i] >= threshold]
    sorted_docs = sorted(filtered_docs, key=lambda x: x[2], reverse=True)
    
    
    return sorted_docs[:top_k]

