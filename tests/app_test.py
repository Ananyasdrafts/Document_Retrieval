import unittest
import json
from app import app, db
from unittest.mock import patch

class FlaskAppTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = app
        cls.client = cls.app.test_client()
        cls.app.config['TESTING'] = True
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        cls.db = db
        cls.db.create_all()

    @classmethod
    def tearDownClass(cls):
        cls.db.drop_all()

    def setUp(self):
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_health_check(self):
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "API is running!"})

    @patch('app.perform_search')
    def test_search(self, mock_search):
        mock_search.return_value = [{'id': 1, 'similarity': 0.9, 'text': 'Test article'}]
        response = self.client.post('/search', 
                                    data=json.dumps({'user_id': 'test_user', 'text': 'Test search'}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('data', response.json)
        self.assertEqual(response.json['data'], [{'id': 1, 'similarity': 0.9, 'text': 'Test article'}])

    @patch('app.get_cached_results')
    @patch('app.cache_search_results')
    def test_cache(self, mock_cache, mock_get_cache):
        mock_get_cache.return_value = None
        mock_cache.return_value = None

        response = self.client.post('/search', 
                                    data=json.dumps({'user_id': 'test_user', 'text': 'Cache test'}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('data', response.json)
        mock_cache.assert_called_once()

    def test_rate_limiting(self):
        # Add a user to the database
        db_session = db.SessionLocal()
        user = db.User(user_id='rate_limit_user', frequency=5)
        db_session.add(user)
        db_session.commit()
        db_session.close()

        response = self.client.post('/search', 
                                    data=json.dumps({'user_id': 'rate_limit_user', 'text': 'Rate limit test'}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 429)
        self.assertEqual(response.json, {"error": "Too many requests"})

if __name__ == '__main__':
    unittest.main()
