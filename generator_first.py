def number(n):
    for i in range(1, n+1):
        yield i

for num in number(10):
    print(num)



def all_even(n):
    for i in range(2, n+1, 2):
            yield i

for i in all_even(10):
    print(i)


