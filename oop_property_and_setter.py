class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = max(price, 0)

    @property
    def complete_specification(self):
        return f"{self.brand} {self.model} price is {self.price}"

    @property
    def modified_price(self):
        return self.price

    @modified_price.setter
    def modified_price(self, new_price):
        self.price = max(new_price, 0)
   
phone1 = Phone('Nokia', '1150', 1200)

phone1.price = -1500
print(phone1.price)
print(phone1.complete_specification)