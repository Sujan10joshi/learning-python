class Person:
    def __init__(self, first_name, last_name, age):
        print("init method / constructor called")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

p1 = Person('Sujan', 'Joshi', 23)
p2 = Person('Harry', 'Michale', 35)

print(p1.first_name)
# print(p2.last_name)