def all_even(n):
    for i in range(2, n+1, 2):
            yield i

for i in all_even(10):
    print(i)