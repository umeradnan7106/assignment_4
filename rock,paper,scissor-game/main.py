# Rock Paper Scissors Game
import random

choices = ["rock", "paper", "scissor"]

player_choice = input("Enter a choice (rock, paper, scissor): ").lower()

computer_choice = random.choice(choices)

print(f"You chose {player_choice}, computer chose {computer_choice}")

# Check if the player's choice is valid
if player_choice not in choices:
    print("Invalid choice. Please try again.")
    exit()


if player_choice == computer_choice:
    print("It's a tie!")
elif(
    (player_choice == "rock" and computer_choice == "scissor") or
    (player_choice == "paper" and computer_choice == "rock") or
    (player_choice == "scissor" and computer_choice == "paper")
):
    print("You win!")
else:
    print("You lose!")