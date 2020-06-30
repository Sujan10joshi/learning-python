class Normalphones:  #base class/ parent class
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price, 0)

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def make_a_call(self, number):
        return f"Calling {number} ...."
    
class Smartphones(Normalphones):   #derived class / child class
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera):
        Normalphones.__init__(self, brand, model_name, price)  #uncommom way to inherit
        # super().__init__(brand, model_name, price)
        self.ram =ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera
    
    def full_name(self):
        return f"{self.brand} {self.model_name} and price is {self._price}"

            # Multilevel inheritance
class FlexshipPhones(Smartphones):
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera, processor, front_camera):
        super().__init__(brand, model_name, price, ram, internal_memory, rear_camera)
        self.processor = processor
        self.front_camera = front_camera


noramalphone1 = Normalphones('Nokia', '1150', 1200)
smartphone1 = Smartphones('I-phone', '11 max pro', 90000, '6 Gb', '128 Gb', '48 MP')
flexship1 = FlexshipPhones('Redmi', 'Note 9 pro', 45000, '8 GB', '128 GB', '48 MP', '2.25 Mgz', '20 MP')

# print(noramalphone1.full_name())
# print(flexship1.full_name() + f" and price is {flexship1._price}")

print(flexship1.full_name())
# print(help(FlexshipPhones))    # Method Resolution Order (MRO)

print(isinstance(flexship1, Normalphones))
print(issubclass(Smartphones, Normalphones))