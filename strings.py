first_name = "Sujan"
Last_name = "Joshi"

full_name = first_name + " " + Last_name
print(full_name)
print(full_name + str(7))
print(first_name * 4)

#user input

name=input("Type your Name\t")
print("Hello", name)
age =input("your age?\t")
print('my age is ' + age)

#string formatting

name, age = "sujan ", 22
print("\nHello " + name + "your age is " + str(age))
print("Hello {} your age is {}".format(name,age)) #python 3
print(f"Hello {name} your age is {age}")
