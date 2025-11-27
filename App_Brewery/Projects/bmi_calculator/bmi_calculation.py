# Body mass index

height = 1.85
weight = 84

bmi = weight / (height ** 2)

print(bmi)

if bmi < 18.5:
    print("Your are Underweight!")
elif bmi >= 18.5 and bmi < 25:
    print("Your weight is normal!")
else:
    print("You are Overweight!")
    