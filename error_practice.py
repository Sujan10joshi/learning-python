def division(a,b):
    try:
        return a/b
    except TypeError as err:
        print(err)
        # print("please input int num only")
    except ZeroDivisionError:
        print("don\'t divide by zero")
    except:
        print("unexpected error...")

print(division(4,'0'))