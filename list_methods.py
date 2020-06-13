fruits = ['apple', 'mango', 'grapes', 'banana', 'kiwi', 'mango', 'pine']
print(fruits.count('mango'))

numbers = [3,9,1,6,29,17,24,8]
#numbers.sort()
#print(sorted(numbers))
#numbers.clear()
number_copy = numbers.copy()
print(number_copy)


fruits1 = ['apple', 'mango', 'grapes']
fruits2 = ['banana', 'kiwi', 'mango', 'pine']
fruits3 = ['apple', 'mango', 'grapes']
print(fruits1 == fruits3) #values same
print(fruits1 is fruits3) #memory placement different
