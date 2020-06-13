num = input("Enter any more than one digits: ")
print(f"length is: {len(num)}")
sum = 0
i = 0
while i < len(num):
    sum += int(num[i])
    i += 1
print(sum)

