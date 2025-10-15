student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78,65, 89, 86]

max_number = student_scores[0]

for number in student_scores:
    if number > max_number:
        max_number = number

print(max_number)

# total sum

sum_numbers = 0

for score in student_scores:
    sum_numbers += score

print(sum_numbers)