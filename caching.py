import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

def cache_search_results(cache_key, search_results):
    
    r.setex(cache_key, 3600, str(search_results))

def get_cached_results(cache_key):
    cached_response = r.get(cache_key)
    if cached_response:
        return cached_response.decode('utf-8')
    return None
