winning_number = 30
guessed_number = input("Enter correct number: ")
guessed_number = int(guessed_number)
if winning_number == guessed_number:
    print("CONGRATS! ***YOU WIN*** ")
else:
    if winning_number > guessed_number:
        print("Too Low")
    else:
        print("Too High") 