name, alpa=input("Enter any name and single character seperate by comma: ").split(",")
print(f"Length of your name is: {len(name)}")
print(f"Character count is: {name.strip().lower().count(alpa.strip().lower())}")


# name.strip().lower().count(alpa.strip().lower())
