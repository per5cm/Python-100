import random

rock = r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = r"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

players_choices = [rock, paper, scissors]
computer_choices = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print("Player chose: ")
print(players_choices[player_choice])

random_index = random.randint(0, 2)
print(f"Computer chose: {computer_choices[random_index]}")

if player_choice < random_index:
    print("Computer Wins!")
elif player_choice > random_index:
    print("Player Wins!")
else:
    print("Its a Draw!")
