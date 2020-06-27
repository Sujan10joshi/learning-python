# def myfunc(func, l):
#     new_list = []
#     for item in l:
#         new_list.append(func(item))
#     return new_list

def my_func(func,l):
    return [func(item) for item in l]

print(my_func(lambda a: a**3, [1,3,5,7]))