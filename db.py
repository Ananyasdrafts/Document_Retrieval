from sqlalchemy import create_engine, Column, Integer, String, Float, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database setup
DATABASE_URL = "postgresql://ananya:mde6133#K@localhost/doc_retrieval"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, index=True)
    frequency = Column(Integer, default=0)

class Document(Base):
    __tablename__ = 'documents'
    doc_id = Column(Integer, primary_key=True, index=True)
    document_text = Column(String)
    document_embedding = Column(ARRAY(Float))  # Store embedding as an array of floats

# Create tables
Base.metadata.create_all(bind=engine)
