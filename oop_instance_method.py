    #instance methods
class Person:
    def __init__(self, first_name, last_name, age):
        self.first = first_name
        self.last = last_name
        self.age = age
    
    def full_name(self):    #instance method
        return f"{self.first} {self.last}"

    def is_above(self): #instance method
        return self.age > 18

p1 = Person('Sujan', 'Joshi', 8)
p2 = Person('Lionel', 'Messi', 33)

# print(p1.full_name())
# print(p2.full_name())

print(p1.is_above())