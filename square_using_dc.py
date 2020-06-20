square = {f"square of {num}" : num**2 for num in range(1,11)}
for k, v in square.items():
    print(f"{k} : {v}")

strings = "sujanankamzx"
counter = {char:strings.count(char) for char in strings}
print(counter)