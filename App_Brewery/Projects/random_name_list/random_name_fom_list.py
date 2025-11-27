import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

print(random.choices(friends, weights=None, cum_weights=None, k=1))

print(random.choice(friends))

# 2nd Option

random_index = random.randint(0, 4)
print(friends[random_index])