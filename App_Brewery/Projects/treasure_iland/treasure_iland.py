from App_Brewery.Projects.treasure_iland.treasure_iland_ascii_art import art

print(art)

print("\nWelcome to Treasure Island!")
print("Your mission is to find the treasure.")

print("\nYou're at a cross road. Where do you want to go?")

## my solution. bit messy.
direction = input("Type 'left' or 'right': \n").lower()

if direction == "right":
    print("Fall into a hole. Game Over")
elif direction == "left":
    print("You\'ve come to a lake. There is an island in the middle of the lake.")
    
    action = input("Type 'swim' or 'wait'?: \n").lower()
    if action == "swim":
        print("Attacked by trout. Game Over.")
    elif action == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        
        color = input("One 'red', one 'yellow' and one 'blue'. Which colour do you choose?: \n").lower()
        if color == "red":
            print("Burned by fire. Game Over.")
        elif color == "blue":
            print("Eaten by beasts. Game Over.")
        elif color == "yellow":
            print("You Win!")
        else:
            print("Game Over.")

## the other way.
# choice1 = input("\nYou're at a cross road. Where do you want to go? Type 'left' or 'right': \n").lower()

# if choice1 == "left":
#     choice2 = input("You\'ve come to a lake. There is an island in the middle of the lake.Type 'swim' or 'wait'?: \n").lower()
#     if choice2 == "wait":
#         choice3 = input("You arrive at the island unharmed. There is a house with 3 doors.One 'red', one 'yellow' and one 'blue'. Which colour do you choose?: \n").lower()
#         if choice3 == "yellow":
#             print("You found the treasure. You Win!")
#         elif choice3 == "red":
#             print("Its a room full of fire. Game Over.")
#         elif choice3 == "blue":
#             print("You enter a room of beasts. Game Over.")
#         else:
#             print("You chose a door that doesnt exist. Game Over.")
#     else:
#         print("You got attacked by an angry trout. Game Over.")
# else:
#     print("Fall into a hole. Game Over.")