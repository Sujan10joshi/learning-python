number1 = [2,4,6,8,10]
number2 = [1,2,3,9,5,11]

# result = []
# for num in number1:
#     result.append(num%2==0)

# print(result)

result = all([num%2==0 for num in number1])
print(result)

new_result = any([num%2==0 for  num in number2])
print(new_result)