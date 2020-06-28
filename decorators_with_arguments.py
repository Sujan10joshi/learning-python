from functools import wraps
def only_data_type_allow(any_data_type):
    def decorator_data_type(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if all([type(arg)==any_data_type for arg in args]):
                return function(*args, **kwargs)
            return 'Invalid argument'
        return wrapper
    return decorator_data_type

@only_data_type_allow(str)
def string_conc(*args):
    string = ''
    for i in args:
        string += i
    return string

print(string_conc('sujan', 'joshi',8))