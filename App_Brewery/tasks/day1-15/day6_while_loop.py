# For
# for item in list_of_items:
#   # Do something to each item

# for number in range(a, b):
#   print(number)

# While
# while something_is_true:
#   # Do something repeatedly

# Infinite loop

# while 5 > 3:
#     print(5 > 3)
#     print("Hello World")

# Reeborg's World
def jump():
    jump()

number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
    print(number_of_hurdles)

# Reborg's World 
while not at_goal():
    if front_is_clear():
        move()
        
    elif wall_in_front():
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
        

print("im here!")