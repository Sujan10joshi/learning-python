class Bikes:
    discount_percentage = 10  #Bikes.discount_percentage discounts in class
    def __init__(self, bike_name, price):
        self.name = bike_name
        self.price = price

    def apply_discount(self):
        return self.price - (self.discount_percentage/100)*self.price #self.discount_percentage discounts in objec

bike1 = Bikes('Duke 200', 550000)
bike2 = Bikes('Bullet 500', 756000)
bike3 = Bikes('Vespa 150', 215000)
bike1.discount_percentage = 50

print(bike1.__dict__)
print(bike1.apply_discount()) 

print(bike2.__dict__)
print(bike2.apply_discount())