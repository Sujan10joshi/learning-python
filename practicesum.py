num = input("Enter number: ")
num = int(num)
total = 0

for i in range (0, len(num)):
    total += int(num[i])
print(total)