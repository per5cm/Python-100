# Overflow

# Conditional if/ else

# if condition:
#   di this
# else:
#   do this

print("Welcome to the rollecoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollecoaster")
else:
    print("Sorry you hvae to gorw taller before you can ride.")
    
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to
# == Equal to
# != not equal to


# Neste if/ else

# if condition:
#   if another condition:
#       do this
#   else:
#       do this
# else:
#   do this

print("Welcome to the rollecoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollecoaster")
    age = int(input("What is your age? "))
    if age <= 18:
        print("Please pay 7€.")
    else:
        print("Please pay 12€")
else:
    print("Sorry you hvae to gorw taller before you can ride.")


# if / elif / else

# if conditions1:
#   do A
# else:
#   do this

print("Welcome to the rollecoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollecoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay 5€.")
    elif age <= 18:
        print("Please pay €7")
    else:
        print("Please pay 12€")
else:
    print("Sorry you hvae to gorw taller before you can ride.")
    
# Multiple if

# if condition1:
#   do A
# if condition2:
#   do B
# if condition3:
#   do C

print("Welcome to the rollecoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollecoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets 5€.")
    elif age <= 18:
        bill = 7
        print("Youth tickets €7")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets 12€")
    wants_photo = input("Do you wanna photo taken? Type y for Yes and n for No.: ").lower()
    if wants_photo == "y":
        # add 3€ to a bill
        bill += 3
    print(f"Your final bill is: {bill}€")
        
else:
    print("Sorry you hvae to gorw taller before you can ride.")