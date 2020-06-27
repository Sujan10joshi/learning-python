# def outer_func():
#     def inner_func():
#         print("Inside inner function.")
#     return inner_func

# var = outer_func()
# var()


# def outer_func2(msg):
#     def inner_func2():
#         print(f"message is {msg}")
#     return inner_func2
# var2 = outer_func2('hello there')
# var2()


def to_power(x):
    def calc_num(n):
        return n**x
    return calc_num

cube = to_power(3)
print(cube(3))

square = to_power(4)
print(square(4))