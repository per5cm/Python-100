print("Welcome to Tip Calculator!\n")

bill_cost = float(input("What was the total bill?: "))
tip_given = float(input("How much tip would you like to give in %?: 10, 12, or 15?: "))
split_people = float(input("How many people to split the bill?: "))

total_sum = round(bill_cost * (1 + tip_given / 100) / split_people, 2)

print(f"Each person should pay: {total_sum:.2f}")