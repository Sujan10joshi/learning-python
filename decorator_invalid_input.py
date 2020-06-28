from functools import wraps
def only_int_allow(any_func):
    @wraps(any_func)
    def wrapper(*args, **kwargs):
        if all([type(arg)==int for arg in args]):
            return any_func(*args, **kwargs)
        return 'Invalid Arguments'
        # data_types = []
        # for arg in args:
        #     data_types.append(type(arg)==int)
        # if all(data_types):
        #     return any_func(*args, **kwargs)
        # else:
        #     print("Invalid Input")
    return wrapper

@only_int_allow
def add_all(*args):
    total = 0
    for i in args:
        total += i
    return total

print(add_all(1,2,3,5, 'sujan'))

