from functools import wraps
def decorator_func(any_func):
    @wraps(any_func)
    def wrapper_func(*args, **kwargs):
        ''' This is wrapper function '''
        print("Awesome function.")
        return any_func(*args, **kwargs)
    return wrapper_func

@decorator_func
def add_func(a,b):
    '''This is add function. '''
    return a+b
print(add_func(4,5))

print(add_func.__doc__)
print(add_func.__name__)