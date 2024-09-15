# 21BCE3537_ML

# Document Retrieval System for Chat Applications

Welcome to the Document Retrieval System! This project provides an efficient way to retrieve documents based on textual queries, designed to enhance chat applications. Leveraging Flask, PostgreSQL, Redis, and Sentence-BERT, it ensures fast and relevant document retrieval.

## Features

1. **Document Ingestion**: 
   - Store and manage documents in a PostgreSQL database.
2. **Query-Based Search**: 
   - Retrieve and rank documents using Sentence-BERT embeddings for query similarity.
3. **Caching for Performance**: 
   - Utilize Redis to cache frequently accessed search results, reducing response times.
4. **Background Scraping**: 
   - Periodically scrape news articles from RSS feeds to keep the document store updated.

## Logging and Performance Monitoring

- **Inference Time**: Logs the time taken to complete each inference request.
- **API Logging**: Records logs for each API call and handles errors, including rate limiting.

## Re-Ranking Algorithm

- **BM25 Re-Ranking**: Enhances document ranking by combining Sentence-BERT embeddings with BM25 scoring.

## Repository Structure

- `app.py`: Main Flask application
- `db.py`: Database configuration and models (PostgreSQL)
- `search.py`: Search logic using Sentence-BERT
- `scraping.py`: Background scraping logic (RSS feeds)
- `caching.py`: Redis caching logic
- `Dockerfile`: Docker configuration file
- `requirements.txt`: Python dependencies
- `tests/`: Unit tests for the application
  - `test_app.py`: Sample unit tests for the Flask application

## Prerequisites

- Python 3.x
- PostgreSQL
- Redis
- Required Python libraries (listed in `requirements.txt`)

## Setup Instructions

1. **Clone the Repository**: 
   ```bash
   git clone <repository-url>
   cd <repository-directory>

2. **Install Dependencies:**: 
   ```bash
   pip install -r requirements.txt

3. **Configure PostgreSQL and Redis:**
   - Update database credentials in `db.py`.
   - Update Redis connection settings in `caching.py`.

4. **Start the Flask Application:**: 
   ```bash
   python app.py
5. **Run the Background Scraper:**
    The background scraping is automatically started with the Flask application. Ensure the URLs in 
    `scraping.py` are set to your sources.


### Usage

- **Start the server**: Once the setup is complete, interact with the system via the API for text queries. Use the /search endpoint to query documents.
- **Run Background Scraping**: Keep the scraper running to ensure the document store remains updated with fresh content.

## License

This project is licensed under the GNU General Public License v3.0. See the LICENSE file for more details.

## Contributions

Contributors: recruitments@trademarkia.com

## Author

Ananya Gupta - 21BCE3537
