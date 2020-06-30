class Phones:
    def __init__(self, brand, model, price):
        self.brand =brand
        self.model = model
        self.price =price

    def phone_name(self):
        return f"{self.brand} {self.model}"

    def __len__(self):
        return len(self.phone_name())

    def __str__(self):            #normal users
        return f"{self.brand} {self.model} and price is {self.price}"    

    def __repr__(self):             #for developers
        return f"Phones(\'{self.brand}\', \'{self.model}\', {self.price})"

    def __mul__(self, other):
        return self.price * other.price


class Smartphones(Phones):
    def __init__(self, brand, model, price, camera):
        super().__init__(brand, model, price)
        self.camera =camera
    
    def phone_name(self):
        return f"{self.brand} {self.model} and price is {self.price}"


my_phone = Phones('Nokia', '1150', 1200)
my_phone2 = Phones('Nokia', '1550', 1500)
my_smartphone = Smartphones('Samsung', 'A 50', 45000, '48 MP')

# print(my_phone.__repr__())

# print(len(my_phone))

# print(my_phone * my_phone2)

print(my_smartphone.phone_name())