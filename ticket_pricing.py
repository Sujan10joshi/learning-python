user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
user_age = int(user_age)
if 0 < user_age <= 3:
    print("Ticket is Free!")
elif 3 < user_age <= 12:
    print("Ticket price is Rs. 100")
elif 12 < user_age <= 20:
    print("Ticket price is Rs. 150")
else:
    print("Ticket price is Rs.200") 