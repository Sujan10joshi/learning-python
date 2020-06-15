# user_info = {
#     'name' : 'Sujan',
#     'age' : 23,
#     'fav_nums' : [5,7,10],
#     'fav_movies' : ['Kabir Singh', 'Dear Comrade', 'Love Aaj Kal']
# }

user_info = dict(
    name = 'Sujan',
    age = 23,
    fav_nums = [5,7,10],
    fav_movies = ['Kabir Singh', 'Dear Comrade', 'Love Aaj Kal']
)

print(user_info['name'])

#add data
user_info['fav_songs'] = ['Laija re', 'Love me']

#pop data
popped_item = user_info.pop('fav_nums')
print(f"popped item is {popped_item}")

#popitem method ----- randomly pop one item
poped_item = user_info.popitem()
print(poped_item)

print(user_info)