# Mersenne Twister
# pseudo random numbers

import random
import day4_my_module

# random_integer = random.randint(1, 10)
# print(random_integer)

print(day4_my_module.my_favorite_number)

# random_number_0_to_1 = random.random() * 10 # semi open range
# print(random_number_0_to_1)

# random_float = random.uniform(1, 10)
# print(random_float)

random_coin = random.randint(1, 2)
if random_coin > 1:
    print("Heads")
else:
    print("Tails")