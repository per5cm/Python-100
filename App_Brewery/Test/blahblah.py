# age = int(input("Wie alt sind Sie?: "))
# if age < 18:
#     print("Zu jung!")
# else:
#     print("Passt")

direction = input("Welche wärung möchten wechseln? e = EUR zu dollar, d = Dollar zu euro: ")
total_sum = float(input("Wie viel geld möchten Sie wechseln?: "))

euro_to_dollar = 1.19
dollar_to_euro = 0.84


if direction == "e":
    final_sum = round(euro_to_dollar * total_sum)
elif direction == "d":
    final_sum = round(dollar_to_euro * total_sum)

print(f"Die wechsell summe ist: €{final_sum:.2f}")