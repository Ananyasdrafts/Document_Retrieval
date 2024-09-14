import time
from newspaper import Article
from db import SessionLocal, Document
from sentence_transformers import SentenceTransformer

# Load the Sentence-BERT model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def scrape_news():
    while True:
        # Scraping logic
        article = Article('http://example.com')  # Example URL; replace with actual scraping logic
        article.download()
        article.parse()
        
        # Encode the article text
        embedding = model.encode(article.text).tolist()
        
        # Save article to the database
        db_session = SessionLocal()
        new_document = Document(
            document_text=article.text,
            document_embedding=embedding
        )
        db_session.add(new_document)
        db_session.commit()
        db_session.close()

        time.sleep(3600)  # Scrape every hour
