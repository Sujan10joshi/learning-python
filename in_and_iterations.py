user_info = {
    'name' : 'Sujan',
    'age' : 23,
    'fav_nums' : [5,7,10],
    'fav_movies' : ['Kabir Singh', 'Dear Comrade', 'Love Aaj Kal']
}

# Check if key exist in dictionary
# if 'name' in user_info:
#     print("Present")
# else:
#     print("Not present")

# Checkif values exxist in dictionary ----- values method
# if 23 in user_info.values():
#     print("Present")
# else:
#     print("Not present")

#looping in dictionaries
# for i in user_info.values():
#     print(i)

# user = user_info.keys()
# print(user)

#Item method
# user_item = user_info.items()
# print(user_item)

for i, j in user_info.items():
    print(f"key is {i} and value is {j}")
