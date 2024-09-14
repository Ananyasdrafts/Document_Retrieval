from flask import Flask, jsonify, request
import time
import threading
from sentence_transformers import SentenceTransformer
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "API is running!"})

if __name__ == "__main__":
    app.run(debug=True)
