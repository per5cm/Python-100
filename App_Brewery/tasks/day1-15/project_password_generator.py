import random
from project_password_lists import letters
from project_password_lists import numbers
from project_password_lists import symbols

print("Welcome to the PyPassword Generator!")

password_lenght = ""


nr_letters = int(input("How many letters would you like in your password?: \n"))
password_lenght.append(nr_letters)
nr_symbols = int(input("How many symbols would you like?: \n"))
password_lenght.append(nr_symbols)
nr_numbers = int(input("How many numbers would you like?: \n"))
password_lenght.append(nr_numbers)

print(password_lenght)
