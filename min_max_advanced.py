# names = ['sujan', 'ram', 'shree krishna']

# def len_name(items):
#     return len(items)

# print(min(names, key= lambda a : len(a)))      #key = len_name



# students = [
#     {'name':'sujan', 'score':99, 'age':23},
#     {'name':'david', 'score':36, 'age':27},
#     {'name':'harrry', 'score':69, 'age':19}
# ]

# max_student = max(students, key = lambda item : item.get('score'))
# print(max_student.get('name'))

# print(max(students, key = lambda items : items.get('score'))['name'])


student2 = {
    'sujan' : {'score':79, 'age':23},
    'shawn' : {'score':47, 'age':19},
    'jonny' : {'score':26, 'age':34}
}

print(max(student2, key = lambda item : student2[item]['score']))