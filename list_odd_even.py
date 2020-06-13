def filter_odd_even(l):
    odd = []
    even = []
    for i in l:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    output = [odd, even]
    return output

numbers = [1, 6, 9, 4, 32, 65, 74, 99, 24, 36, 77]

print(filter_odd_even(numbers))