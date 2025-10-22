import random
from project_password_lists import letters
from project_password_lists import numbers
from project_password_lists import symbols

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?: \n"))
nr_symbols = int(input("How many symbols would you like?: \n"))
nr_numbers = int(input("How many numbers would you like?: \n"))

password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

password = ""
for char in password_list:
    password += char
print("char", char)

pwd = ''.join(password_list)
print(f"Your random password to use is: {pwd}")