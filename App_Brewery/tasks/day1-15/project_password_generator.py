import random
from project_password_lists import random_password

print("Welcome to the PyPassword Generator!")

character_list = " "

while(True):
    nr_letters = int(input("How many letters would you like in your password?: \n"))
    if(nr_letters == 1):
        character_list += nr_letters
    nr_symbols = int(input("How many symbols would you like?: \n"))
    
    character_list += nr_symbols
    nr_numbers = int(input("How many numbers would you like?: \n"))
    character_list += nr_numbers

password = []
print(password)

print(random_password)