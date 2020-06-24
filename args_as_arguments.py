def multiply(*args):
    multi = 1
    for i in args:
        multi *= i
    return multi

nums = [2,3,4]
print(multiply(*nums))  #unpack list