student_heights = input("Input a list of student heights ").split()
addStudentHeight = 0
numberOfHeight = 0

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    addStudentHeight += student_heights[n]
    numberOfHeight += 1
    # print(student_heights)
    # print(addStudentHeight)
print("=*" * 30)
print(round(addStudentHeight / numberOfHeight, 0))
print("=*" * 30)
# for
# 123 112 211 333 555 921
# 156 178 165 171 187
# 180 124 165 173 189 169 146
