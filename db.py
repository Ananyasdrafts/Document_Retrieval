
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import numpy as np

DATABASE_URL = "postgresql://ananya:mde6133#K@localhost/doc_retrieval"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)

class Document(Base):
    __tablename__ = 'documents'
    doc_id = Column(Integer, primary_key=True, index=True)
    document_text = Column(String)
    document_embedding = Column(Float, array=True)

Base.metadata.create_all(bind=engine)

def save_article_to_db(title: str, content: str):
    """
    Save a scraped article to the database.
    """
    db_session = SessionLocal()
    article = Article(title=title, content=content)
    db_session.add(article)
    db_session.commit()
    db_session.close()

def get_documents():
    """
    Retrieve documents and their embeddings from the database.
    """
    db_session = SessionLocal()
    documents = db_session.query(Document).all()
    db_session.close()

    docs_list = [(doc.doc_id, doc.document_text, np.array(doc.document_embedding)) for doc in documents]
    return docs_list
