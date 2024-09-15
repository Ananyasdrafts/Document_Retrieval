# 21BCE3537_ML

# Document Retrieval System for Chat Applications

Welcome to the Document Retrieval System! This project enables efficient retrieval of documents based on textual queries, designed for enhancing chat applications. Using a combination of Flask, PostgreSQL, Redis, and Sentence-BERT, it ensures quick and relevant document retrieval.

The document retrieval system operates through a well-defined pipeline, which includes:

1. **Document ingestion**: Store documents in a PostgreSQL database for easy access and management.
2. **Query-based search**: Retrieve and rank documents using Sentence-BERT embeddings based on query similarity.
3. **Caching for performance**: Cache frequently accessed results using Redis to improve response times.
4. **Background scraping**: Periodically scrape and update the document store with news articles from RSS feeds.

## Logging and Performance Monitoring

- **Inference Time**: Each request will log the time taken for the inference to complete.
- **API Logging**: Logs are generated for each API call, including error handling for rate limiting.

## Bonus Features

- **Re-ranking Algorithm**: BM25 re-ranking is implemented for improving document ranking.

## Repository Structure

- `app.py`: Main Flask application
- `db.py`: Database configuration and models (PostgreSQL)
- `search.py`: Search logic using Sentence-BERT
- `scraping.py`: Background scraping logic (RSS feeds)
- `caching.py`: Redis caching logic
- `Dockerfile`: Docker configuration file
- `requirements.txt`: Python dependencies
- `tests/`: Unit tests for the application
  - `test_app.py`: Sample tests for the app

### Prerequisites

- Python 3.x
- Required libraries in `requirements.txt`

## Setup Instructions

1. Clone the repository and install the required dependencies.
2. Set up PostgreSQL and Redis by configuring credentials in `db.py` and `caching.py`.
3. Start the Flask application and the background scraper.

### Usage

- **Start the server**: Once the setup is complete, interact with the system via the API for text queries.
- **Run Background Scraping**: Keep the scraper running to ensure the document store remains updated with fresh content.

## License

This project is licensed under the GNU General Public License v3.0. See the LICENSE file for more details.

## Author

Ananya Gupta - 21BCE3537
