user_id = ['user1', 'user2', 'user3']
user_name = ['sujan', 'david', 'jackkie']
last_name = ['joshi', 'sharma', 'shrestha']

# print(dict(zip(user_id, user_name,)))

print(list(zip(user_id, user_name, last_name)))

# ex = [('a',1), ('b',2)]
# print(dict(ex))


# reverse of above
nums = [(1,3),(2,4),(5,7),(6,8)]

num1, num2 = zip(*(nums))
print(list(num1))
print(list(num2))

# greater in two list pair
n1 = [1,4,7,5]
n2 = [4,2,6,9]
new_list = []
for pair in zip(n1,n2):
    new_list.append(max(pair))
print(new_list)