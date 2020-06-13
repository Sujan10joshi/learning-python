numbers = list(range(1, 11)) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)

#popped_num = numbers.pop()
#print(popped_num)

#print(numbers.index(5))  

def negative_list(n):
    negative = []
    for i in n:
        negative.append(-i)
    return negative

print(negative_list(numbers))    