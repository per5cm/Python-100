print("\nWelcome to Treasure Island!")
print("Your mission is to find the treasure.")

print("\nYou're at a cross road. Where do you want to go?")

direction = input("Type 'left' or 'right': \n").lower()

if direction == "right":
    print("Fall into a hole. Game Over")
elif direction == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    
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

