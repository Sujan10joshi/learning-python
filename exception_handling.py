while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("may be you entered wrong input..try again")
    except:
        print("unexcpected errror")

if age > 18:
    print("You can play this game.")
else:
    print("You can\'t play this game.")