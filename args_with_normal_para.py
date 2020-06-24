def multiply(num1,num2,*args):
    print(num1)
    print(num2)
    print(args)
    multi = 1
    for i in args:
        multi *= i
    return multi

print(multiply(2,3,4,5))