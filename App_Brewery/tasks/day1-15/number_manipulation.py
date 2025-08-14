# Number Manipulation

bmi = 84/ 1.65 ** 2
print(bmi)

# Floor the number
print(int(bmi)) #30

# Round the number
print(round(bmi)) #31

print(round(bmi, 2)) # rounds to a floating point number with two decimal placments

# Asignment Operator
score = 0

# User scores a point
score +=1 # you can also use -= or *=
print(score)

# f-strings
print("your score is " + str(score))

score_two = 0 #int
height = 1.8 #float
is_winning = True #bool

print(f"Your score is = {score_two}, your height is{height}. Your are winning is {is_winning}")