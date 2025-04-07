# Guess the number game (computer guesses the number)

import random

print("Guess the number between 1 and 10")

number = random.randint(1, 10)

user_guess = int(input("Enter your guess: "))

if user_guess == number:
    print("You guessed the number correctly!")
else:
    print("You guessed the number incorrectly!")


# computer guesses the number

computer_guess = random.randint(1, 10)

if computer_guess == number:
    print("computer guessed the number correctly!")
else:
    print("computer guessed the number incorrectly!")