class Person:
    count_instance = 0
    def __init__(self, name, age):
        Person.count_instance += 1
        self.name = name
        self.age = age

    @classmethod
    def instance_counter(cls):
        return f"You have entered {cls.count_instance} instances of {cls.__name__} class"

p1 = Person('Sujan', 23)
p2 = Person('Torres', 36)
p3 = Person('Boateng', 26)

print(Person.instance_counter())