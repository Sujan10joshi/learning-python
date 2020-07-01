class Animals:
    def __init__(self, name):
        self.name = name

    def sound(self):
        raise NotImplementedError('you have to define this method in subclass')

class Cat(Animals):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return 'meao meao'

class Dog(Animals):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return 'bhow bhow'

doggy = Dog('Rupesh', 'pot')
catty =Cat('suri', 'furi')

print(doggy.sound())
print(catty.sound())