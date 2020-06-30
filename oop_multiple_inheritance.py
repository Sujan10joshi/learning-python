class A:
    def class_a(self):
        return "This is class A"

    def hello(self):
        return "Hello from class A"

class B:
    def class_b(self):
        return "This is class B"

    def hello(self):
        return "Hello from class B"

class C(B,A):
    pass

instance_c = C()

print(instance_c.hello())

