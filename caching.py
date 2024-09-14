import redis


r = redis.StrictRedis(host='localhost', port=6379, db=0)

def get_cached_response(cache_key):
    cached_response = r.get(cache_key)
    if cached_response:
        return cached_response.decode('utf-8')
    return None

def set_cached_response(cache_key, response_data, expiration=3600):
    r.setex(cache_key, expiration, response_data)

