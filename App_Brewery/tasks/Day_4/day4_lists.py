states_of_america = ["Delaware", "Pennsylvania", "New Jersey"]

states_of_america[1] = "Pencilvania"

states_of_america.append("Angelaland")

states_of_america.extend(["Angelaland", "Jack Baver Land"])

print(len(states_of_america))

print(states_of_america)

# nesting lists

fruits = ["1", "2", "3"]
vegetables = ["a", "b", "c"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)