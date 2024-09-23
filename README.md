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

## Tech Stack
- **Flask**: I chose Flask for its simplicity and flexibility. It's lightweight, which makes it easy to build and manage the web application. Its minimalistic nature means I can integrate it smoothly with other components, and it lets me focus on getting the core functionality right without being bogged down by unnecessary complexities.

- **PostgreSQL**: I went with PostgreSQL for its robustness and reliability. It handles complex queries and maintains data integrity, which is crucial for managing the documents. PostgreSQL’s support for the ARRAY type is especially handy for storing Sentence-BERT embeddings efficiently.

- **Redis**: Redis was an obvious choice for caching. Its in-memory data store significantly boosts performance by reducing the load on PostgreSQL and speeding up the retrieval of frequently accessed documents. It’s great for handling high traffic and ensuring that the search results are delivered quickly.

- **Sentence-BERT**: Sentence-BERT is fantastic for generating semantic embeddings. It allows for a deeper understanding of the textual content, which means the document retrieval process is much more accurate. I chose it because it really enhances the relevance of search results by capturing the semantic meaning of the text.

## Logging and Performance Monitoring

- **Inference Time**: Logs the time taken to complete each inference request.
- **API Logging**: Records logs for each API call and handles errors, including rate limiting.

## Re-Ranking Algorithm

- **BM25 Re-Ranking**: Enhances document ranking by combining Sentence-BERT embeddings with BM25 scoring.

## Fine-Tuning Sentence-BERT
Improves the quality of document embeddings by training Sentence-BERT on a specific domain or task, allowing it to better capture nuanced relationships between documents and queries for more relevant search results. Fine tuning script in `fine_tune.py`.

## Repository Structure

- `app.py`: Main Flask application
- `db.py`: Database configuration and models (PostgreSQL)
- `search.py`: Search logic using Sentence-BERT
- `scraping.py`: Background scraping logic (RSS feeds)
- `caching.py`: Redis caching logic
- `Dockerfile`: Docker configuration file
- `fine_tune.py`: Script for fine-tuning Sentence-BERT
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

## Contributing

We welcome contributions to enhance the functionality and features of this app. To contribute, please fork the repository, create a new branch, make your changes, and submit a pull request.

Contributors: recruitments@trademarkia.com

## Contact
For any questions or suggestions, please open an issue in this repository or contact the project maintainer at ananyag1019@gmail.com.

