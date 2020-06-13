import random
winnning_number = random.randint(1,100)
winnning_number = int(winnning_number)
guess = 1
number = int(input("Enter a number between 1 and 100: "))
game_over = False
while not game_over:
    if number == winnning_number:
        print(f"Congrats!!! , You guessed correct answer in {guess} times.")
        game_over = True
    else:
        if number < winnning_number:
            print("too low")
        else:
            print("too high")
        guess += 1
        number = int(input("Guess again: "))