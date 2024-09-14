from flask import Flask, jsonify, request
import time
from db import get_user, create_user, update_user_frequency
from search import perform_search
from caching import cache_response, get_cached_response
from scraping import start_scraping_thread
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(filename='logs/app.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

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
    
    # Handle user frequency and rate limiting
    user = get_user(user_id)
    if user:
        if user.frequency >= 5:
            return jsonify({"error": "Too many requests"}), 429
        update_user_frequency(user)
    else:
        create_user(user_id)
    
    # Check cache for search result
    cache_key = f"search:{text}:{top_k}:{threshold}"
    cached_response = get_cached_response(cache_key)
    
    if cached_response:
        response = jsonify({"data": cached_response})
    else:
        response_data = perform_search(text, top_k, threshold)
        cache_response(cache_key, response_data)
        response = jsonify({"data": response_data})
    
    inference_time = time.time() - start_time
    logging.info(f"Request completed in {inference_time} seconds for user {user_id}")
    return response

if __name__ == "__main__":
    start_scraping_thread()
    app.run(debug=True)
