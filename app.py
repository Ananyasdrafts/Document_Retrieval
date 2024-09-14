from flask import Flask, jsonify, request
import time
import threading
from db import SessionLocal, User
from search import perform_search
from caching import cache_search_results, get_cached_results
from scraping import scrape_rss_feed
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "API is running!"})

@app.route('/search', methods=['POST'])
def search():
    start_time = time.time()
    user_id = request.json.get('user_id')
    text = request.json.get('text', 'default text')
    top_k = request.json.get('top_k', 5)
    threshold = request.json.get('threshold', 0.5)
    
    # Check user frequency and apply rate limiting
    db_session = SessionLocal()
    user = db_session.query(User).filter_by(user_id=user_id).first()
    
    if user:
        if user.frequency >= 5:
            return jsonify({"error": "Too many requests"}), 429
        user.frequency += 1
    else:
        user = User(user_id=user_id, frequency=1)
        db_session.add(user)
    
    db_session.commit()
    db_session.close()

    # Check cache
    cache_key = f"search:{text}:{top_k}:{threshold}"
    cached_response = get_cached_results(cache_key)
    
    if cached_response:
        response = jsonify({"data": cached_response})
    else:
        response_data = perform_search(text, top_k, threshold)
        cache_search_results(cache_key, response_data)
        response = jsonify({"data": response_data})
    
    inference_time = time.time() - start_time
    app.logger.info(f"Request time: {inference_time} seconds")
    return response

def start_scraping_thread():
    threading.Thread(target=scrape_rss_feed, daemon=True).start()

if __name__ == "__main__":
    start_scraping_thread()
    app.run(debug=True)
