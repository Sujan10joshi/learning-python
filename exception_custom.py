class NameTooShort(ValueError):
    pass

def validate(name):
    if len(name) < 7:
        raise NameTooShort('Name is too short')

user_name = input("Enter a name: ")
validate(user_name)
print(f"Hello {user_name}")