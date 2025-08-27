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