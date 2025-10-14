import random
from project_rock_paper_scissors_ascii import ascii_list

player_choice = int(input("\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
if player_choice >= 0 and player_choice <=2:
    print(f"Player chose: {ascii_list[player_choice]}")

computer_choice = random.randint(0, 2)
print(f"\nComputer chose: {ascii_list[computer_choice]}")

if player_choice >= 3 or player_choice < 0:
    print("You typed an invalid number. You lose!\n")
elif player_choice == 0 and computer_choice == 2:
    print("Player Wins!\n")
elif computer_choice == 0 and player_choice == 2:
    print("You lose!\n")
elif player_choice < computer_choice:
    print("Computer Wins!\n")
elif player_choice > computer_choice:
    print("Player Wins!\n")
else:
    print("Its a Draw!\n")
