import time
from newspaper import Article
from db import SessionLocal, Document
from sentence_transformers import SentenceTransformer


model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def scrape_news():
    while True:
        # Example URLs; replace these with actual scraping logic or a list of URLs
        urls = ['https://example.com/article1', 'https://example.com/article2']
        
        for url in urls:
            try:
                article = Article(url)
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
            except Exception as e:
                print(f"Error processing {url}: {e}")

        time.sleep(3600)  