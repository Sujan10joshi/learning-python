name = input('Enter your name: ')  # sujanjoshi
i = 0
temp_var = ""
while i < len(name):
    if name[i] not in temp_var:
        print(f"{name[i]} : {name.count(name[i])}")
        temp_var += name[i]
    i += 1
