while True:
    try:
        number = int(input("enter a number: "))

    except ValueError:
        print("please enter int values...")
    except:
        print("unexpected error...")
    else:
        print(f"user input = {number}")
        break
    finally:
        print("This block print with or without errors.")