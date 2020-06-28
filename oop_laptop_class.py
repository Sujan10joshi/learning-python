class Laptop:
    def __init__(self, laptop_brand, laptop_type, price):
        #instance variables
        self.laptop_company = laptop_brand
        self.laptop_type = laptop_type
        self.laptop_price = price
        self.laptop_name = laptop_brand + ' ' + laptop_type

l1 = Laptop('Dell', 'Gaming', 250000)
l2 = Laptop('Lenovo', 'Programming', 215600)

print(l1.laptop_name)
print(l2.laptop_price)