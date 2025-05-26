import functools

def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query', '') if 'query' in kwargs else args[0]
        print(f"[LOG] Executing query: {query}")
        return func(*args, **kwargs)
    return wrapper
