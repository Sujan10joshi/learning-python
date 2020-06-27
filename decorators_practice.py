from functools import wraps
def decorate_func(any_func):
    @wraps(any_func)
    def wrapper_func(*args, **kwargs):
        print(f"You are calling {any_func.__name__} function.")
        print(f"{any_func.__doc__}")
        return any_func(*args, **kwargs)
    return wrapper_func

@decorate_func
def add(a,b):
    '''This number takes two number as argument and return their sum.'''
    return a+b

print(add(4,5))