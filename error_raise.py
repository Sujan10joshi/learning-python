def add(a,b):
    if (type(a) is int and type(b) is int):
        return a+b
    raise TypeError('Wrong input type')
print(add('2','4'))