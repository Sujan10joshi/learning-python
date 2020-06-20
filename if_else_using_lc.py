nums = list(range(1,11))
new_list = [(i**2) if i%2 == 0 else (-i) for i in nums]
print(new_list)