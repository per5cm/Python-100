import random
from project_password_lists import letters, symbols, numbers

print("Welcome to the PyPassword Generator!")

while True:
    nr_letters = int(input("How many letters would you like in your password?: \n"))
    nr_symbols = int(input("How many symbols would you like in your password?: \n"))
    nr_numbers = int(input("How many numbers would you like in your password?: \n"))
    
    total = nr_letters + nr_symbols + nr_numbers
    if total < 8:
        print("\nPassword must be at least 8 characters total. Try again!")
    else:
        break

password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ''.join(password_list)
print(f"Your random password to use is: {password}")
print(f"Total characters used: {len(password_list)}")