# Hangman Game

import random

words_list = ['python', 'javascript', 'html', 'css']

def display_word(word, guess_letter):
    display = ""
    for letter in word:
        if letter in guess_letter:
            display += letter
        else:
            display += " _ "

    display += " "
    return display

random_word = random.choice(words_list)
guess_letter = set()

attempts = 6


while attempts > 0:

    print("Welcome to Hangman Game!")
    print(f"Word: {display_word(random_word, guess_letter)}")
    print(f"Guesses letters: {', '.join(guess_letter)}")
    print(f"You have {attempts} attempts to guess the word.")

    guess = input("Guess the letter:").lower()
    guess_letter.add(guess)

    if guess in random_word:
        print("Correct!")
    else:
        attempts -= 1

    if "_" not in display_word(random_word, guess_letter):
        print("Congratulations! You win!")
        break

    if attempts == 0:
        print("You lose!")
        print(f"The word was {random_word}")
        break
