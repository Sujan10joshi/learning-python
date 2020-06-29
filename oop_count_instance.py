class Person:
    count_instance = 0  #class veriable
    def __init__(self, full_name, age):
        Person.count_instance += 1
        self.full_name = full_name
        self.age = age

p1 = Person('Sujan Joshi', 23)
p2 = Person('Paulo Dybala', 27)
p3 = Person('Paulo Dybala', 27)

print(Person.count_instance)