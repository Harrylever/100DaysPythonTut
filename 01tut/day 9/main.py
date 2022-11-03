student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        key, value = student, "Outstanding"
        # student_grades[student] = "Outstanding"
    elif score > 80:
        key, value = student, "Exceeds Expectation"
    elif score > 70:
        key, value = student, "Acceptable"
    else:
        key, value = student, "Fail"

    student_grades[key] = value

print(student_grades)