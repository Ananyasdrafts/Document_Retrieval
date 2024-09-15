from sqlalchemy import create_engine, Column, Integer, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import ARRAY


DATABASE_URL = "postgresql://ananya:mde6133#K@localhost/doc_retrieval"


engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


class Document(Base):
    __tablename__ = "documents"
    
    id = Column(Integer, primary_key=True, index=True)
    document_text = Column(Text, nullable=False)
    document_embedding = Column(ARRAY(Float), nullable=False)  


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()

