import time
import feedparser
from db import SessionLocal, Document
from sentence_transformers import SentenceTransformer


model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def scrape_rss_feed():
    feed_urls = [
        'http://rss.cnn.com/rss/cnn_topstories.rss', 
        'http://feeds.bbci.co.uk/news/world/rss.xml',
        'https://www.aljazeera.com/xml/rss/all.xml',
        'http://feeds.reuters.com/reuters/topNews',
        'http://rss.cnn.com/rss/cnn_world.rss',
        'http://feeds.bbci.co.uk/news/technology/rss.xml',
        'https://www.aljazeera.com/xml/rss/middleeast.xml',
        'http://feeds.reuters.com/reuters/businessNews'
    ]
    
    while True:
        for url in feed_urls:
            feed = feedparser.parse(url)
            
            for entry in feed.entries:
                try:
                    
                    article_text = f"{entry.title}\n{entry.description}"
                    
                    
                    embedding = model.encode(article_text).tolist()

                    
                    db_session = SessionLocal()
                    new_document = Document(
                        document_text=article_text,
                        document_embedding=embedding
                    )
                    db_session.add(new_document)
                    db_session.commit()
                    db_session.close()
                except Exception as e:
                    print(f"Error processing entry: {e}")

        time.sleep(3600)  
