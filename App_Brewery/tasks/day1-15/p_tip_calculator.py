print("Welcome to Tip Calculator!\n")

total_bill = float(input("What was the total bill?: €"))
tip_given = float(input("How much tip would you like to give in %?: 10, 12, or 15?: "))
tip_split = float(input("How many people to split the bill?: "))

final_sum = round(total_bill * (1 + tip_given / 100) / tip_split, 2)

print(f"Each person should pay: {final_sum:.2f}")

print("Welcome to the tip calculator!")
print("")