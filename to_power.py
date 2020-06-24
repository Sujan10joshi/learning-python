def to_power(num,*args):
    if args:
        return [i**num for i in args]
    else:
        return "YOu didn't pass arguments."
nums = [2,3,4]
print(to_power(3,*nums))
