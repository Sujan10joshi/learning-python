def decorator_func(any_func):
    def wrapper_func(*args, **kwargs):
        print("This function is really awesome.")
        return any_func(*args, **kwargs)
    return wrapper_func

@decorator_func
def func2(a):
    print(f"This function squares {a} of {a**2} ")
func2(10)

@decorator_func
def func3(a,b):
    return a+b
print(func3(2,4))