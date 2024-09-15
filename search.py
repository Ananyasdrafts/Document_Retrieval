from sentence_transformers import SentenceTransformer
from db import SessionLocal, Document
import numpy as np
from scipy.spatial.distance import cosine
from rank_bm25 import BM25Okapi
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')


def perform_search(text, top_k=5, threshold=0.5):
    
    query_embedding = model.encode(text).tolist()

    
    db_session = SessionLocal()
    documents = db_session.query(Document).all()
    db_session.close()

    
    results = []
    document_texts = []  

    for doc in documents:
        
        similarity = 1 - cosine(query_embedding, doc.document_embedding)
        if similarity >= threshold:
            results.append((doc.doc_id, similarity, doc.document_text))
            document_texts.append(doc.document_text)  

    # BM25 Re-ranking on the top-k Sentence-BERT results
    if results:
        tokenized_corpus = [word_tokenize(doc.lower()) for doc in document_texts]
        bm25 = BM25Okapi(tokenized_corpus)
        tokenized_query = word_tokenize(text.lower())
        
        
        bm25_scores = bm25.get_scores(tokenized_query)
        
        
        combined_results = [
            (results[i][0], results[i][1] * 0.5 + bm25_scores[i] * 0.5, results[i][2])  # 50-50 weight for BERT & BM25
            for i in range(len(results))
        ]
        combined_results.sort(key=lambda x: x[1], reverse=True)

        return combined_results[:top_k]
    
    return []