# 21BCE3537_ML


# Document Retrieval System for Chat Applications

## Overview

This project implements a document retrieval system designed for chat applications, which generates context for Large Language Models (LLMs) during inference. The system is built using Flask, PostgreSQL for document storage, Redis for caching, and a background process that periodically scrapes news articles. The system is Dockerized for easy deployment and scalability.

## Problem Statement

The goal is to build a backend for document retrieval that serves as a context generator for chat-based applications. The backend should store documents in a database, retrieve and rank documents based on text queries, cache the results for faster retrieval, and run background scraping for news articles.

## Features

- **Document Retrieval**: Retrieve documents from a PostgreSQL database, rank them using Sentence-BERT embeddings, and return the top results based on query similarity.
- **Caching**: Cache search results using Redis to ensure faster retrieval of frequently queried documents.
- **Background Scraping**: Scrape news articles from RSS feeds at regular intervals and store them in the database.
- **Rate Limiting**: Implement rate-limiting logic, allowing each user to make up to 5 API requests before receiving an HTTP 429 status code.
- **API Endpoints**:
  - `/health`: Returns a status message to check if the API is running.
  - `/search`: Retrieves the top search results for a given query.
- **Dockerized**: The application is Dockerized for easy deployment.

## Requirements

- **Programming Language**: Python (Flask preferred)
- **Database**: PostgreSQL for document storage
- **Document Encoder**: Sentence-BERT or any encoder of your choice
- **Caching**: Use Redis for caching to improve performance
- **Background Processing**: Implement a background thread to scrape news articles as soon as the server starts
- **Endpoints**:
  - `/health`: Check API health
  - `/search`: Search documents with the following parameters:
    - `text`: The search query text
    - `top_k`: Number of results to return (default is 5)
    - `threshold`: Minimum similarity score for document retrieval (default is 0.5)
- **Rate Limiting**: If a user makes more than 5 requests, return an HTTP 429 status code
- **Logging**: Log inference time and other API-related metrics
- **Dockerized**: Application must be containerized and served using Docker

## Setup Instructions

### Prerequisites

- **Python 3.9+**
- **PostgreSQL**: Ensure PostgreSQL is installed and running on your system.
- **Redis**: Install and run Redis for caching.
- **Docker**: Install Docker if you wish to run the project inside a container.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/document-retrieval-system.git
   cd document-retrieval-system
   ```

2. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup the PostgreSQL Database**:
   - Open PostgreSQL terminal:
     ```bash
     psql postgres
     ```
   - Create a new database and user:
     ```sql
     CREATE DATABASE doc_retrieval;
     CREATE USER yourusername WITH PASSWORD 'yourpassword';
     GRANT ALL PRIVILEGES ON DATABASE doc_retrieval TO yourusername;
     ```

4. **Update the Database URL in `db.py`**:
   Replace the `DATABASE_URL` in `db.py` with your PostgreSQL connection string:
   ```python
   DATABASE_URL = "postgresql://yourusername:yourpassword@localhost/doc_retrieval"
   ```

5. **Ensure Redis is running**:
   ```bash
   redis-server
   ```

### Running the Application

1. **Run the Flask Application**:
   ```bash
   python app.py
   ```

   The server should be running on `http://localhost:5000`.

2. **Docker Setup (Optional)**:
   If you prefer to run the project inside Docker:

   - Build the Docker image:
     ```bash
     docker build -t document-retrieval .
     ```
   - Run the Docker container:
     ```bash
     docker run -p 5000:5000 document-retrieval
     ```

### API Endpoints

#### 1. **Health Check**

- **Endpoint**: `/health`
- **Method**: `GET`
- **Description**: Returns a random response to check if the API is active.
- **Response**:
  ```json
  { "status": "API is running!" }
  ```

#### 2. **Search**

- **Endpoint**: `/search`
- **Method**: `POST`
- **Description**: Retrieves top results for the query.
- **Request Body**:
  ```json
  {
    "user_id": 1,
    "text": "search query",
    "top_k": 5,
    "threshold": 0.5
  }
  ```
- **Response**:
  ```json
  {
    "data": [
      { "document_text": "Document 1", "similarity": 0.85 },
      { "document_text": "Document 2", "similarity": 0.80 }
    ]
  }
  ```

- **Rate Limiting**: If the user makes more than 5 requests, the API will return:
  ```json
  { "error": "Too many requests" }
  ```

## Unit Testing

1. **Install `pytest`**:
   ```bash
   pip install pytest
   ```

2. **Create test cases** in the `tests` directory (e.g., `tests/test_app.py`).

3. **Run the tests**:
   ```bash
   pytest
   ```

## Dockerization

1. **Create Docker Image**:
   ```bash
   docker build -t document-retrieval .
   ```

2. **Run Docker Container**:
   ```bash
   docker run -p 5000:5000 document-retrieval
   ```

## Logging and Performance Monitoring

- **Inference Time**: Each request will log the time taken for the inference to complete.
- **API Logging**: Logs are generated for each API call, including error handling for rate limiting.

## Bonus Features

- **Re-ranking Algorithm**: BM25 re-ranking can be implemented for improving document ranking.
- **Fine-tuning Sentence-BERT**: The model can be fine-tuned on domain-specific data for improved accuracy.

## Future Enhancements

1. **Implement Re-ranking Algorithms** like BM25 for better search accuracy.
2. **Fine-tune Sentence-BERT** using custom data to improve performance on specific queries.
3. **Expand Scraping** to include more sources or other types of documents.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

Ananya Gupta
