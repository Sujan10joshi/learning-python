class Mobiles:
    def __init__(self, name):
        self.name = name

class Mobilestore:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self, new_mobile):
        if isinstance(new_mobile, Mobiles):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError('new mobile should be object of mobiles class')

mobile1 = Mobiles('Iphone 11 max')
new_phone = 'Readmi Note 9 pro'
mobistore = Mobilestore()

# print(mobile1.name)
# print(mobistore.mobiles)
mobistore.add_mobile(mobile1)


# print(mobistore.mobiles)

first_phone = mobistore.mobiles
print(first_phone[0].name)
