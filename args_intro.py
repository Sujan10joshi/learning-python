def all_total(*args):  #creates tuple
    total = 0
    for num in args:
        total += num
    return total

print(all_total(1,3,6))