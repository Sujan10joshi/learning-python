class Bikes:
    def __init__(self, bike_name, price):
        self.name = bike_name
        self.price = price

    def apply_discount(self, discount_percent):
        return self.price - (discount_percent/100)*self.price

bike1 = Bikes('Duke 200', 550000)
bike2 = Bikes('Bullet 500', 756000)
bike3 = Bikes('Vespa 150', 215000)

print(bike1.apply_discount(50))
print(bike3.apply_discount(20))