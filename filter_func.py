# def is_even(a):
#     return a%2 == 0

numbers = [1,4,6,3,2,7,8,12,15,35,64,32,21]
#evens = tuple(filter(is_even, numbers))

evens = tuple(filter(lambda a: a%2 == 0, numbers))
print(evens)