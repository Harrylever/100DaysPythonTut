student_scores = input("Input a list of student heights ").split()
current_highest_number = 0

print(student_scores)

# 156 178 165 171 187

for student_score in student_scores:
    student_score = int(student_score)
    if student_score > current_highest_number:
        current_highest_number = 0
        current_highest_number += student_score
#   if student_score > current_highest_number:
#       current_highest_number = student_score
print(f"The highest score in the class is: {current_highest_number}")

