nums = [1,2,3,4,5]

# def square(l):
#     return l**2

# squares = list(map(square, nums))
# print(squares)

squares = list(map(lambda a: a**2, nums))
print(squares)

names = ['abc','abcd','abcde']
length = list(map(len,names))
print(length)