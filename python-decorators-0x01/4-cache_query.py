import functools

query_cache = {}

def cache_query(func):
    @functools.wraps(func)
    def wrapper(conn, query):
        if query in query_cache:
            print("[CACHE] Returning cached result.")
            return query_cache[query]
        result = func(conn, query)
        query_cache[query] = result
        return result
    return wrapper
