from functools import wraps
import time
def calculate_time(any_func):
    @wraps(any_func)
    def wrapper(*args, **kwargs):
        print(f"Executing {any_func.__name__} function...")
        t1 = time.time()
        returned_value = any_func(*args, **kwargs)
        t2 = time.time()
        total_time = t2-t1
        print(f"{any_func.__name__} takes {total_time} seconds to execute.")
        return returned_value
    return wrapper

@calculate_time
def square(n):
    return [i**2 for i in range(1, n+1)]

print(square(10))

