number = list(range(1,11))
print(number)

def square_list(n):
    square = []
    for i in n:
        square.append(i*i)
    return square

print(square_list(number))