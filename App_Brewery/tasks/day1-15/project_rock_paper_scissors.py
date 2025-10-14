import random
from project_rock_paper_scissors_ascii import ascii_list

player_choice = int(input("\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
print("\nPlayer chose: ")
print(ascii_list[player_choice])

random_index = random.randint(0, 2)
print(f"\nComputer chose: {ascii_list[random_index]}")

if player_choice < random_index:
    print("Computer Wins!\n")
elif player_choice > random_index:
    print("Player Wins!\n")
else:
    print("Its a Draw!\n")
