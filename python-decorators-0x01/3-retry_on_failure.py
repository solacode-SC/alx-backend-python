import time
import functools

def retry_on_failure(retries=3, delay=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"[WARN] Attempt {attempt + 1} failed: {e}")
                    time.sleep(delay)
            raise Exception(f"[ERROR] All {retries} attempts failed.")
        return wrapper
    return decorator
