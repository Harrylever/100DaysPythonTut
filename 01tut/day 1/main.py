# Body mass index calculator

user_weight = int(input("Enter your weight in (kg): "))
user_height = input("Enter your height in (m2): ")
if type(user_height) == str:
    user_float_height: float = float(user_height)
    user_float_height = user_float_height ** 2
    bmi = user_weight / user_float_height
    print(int(bmi))
    # print(type(bmi))
else:
    print("Nice")
# user_height2 = user_height ** 2
#
# print("Your height is " + str(user_height) + "\nYour weight is " + str(user_weight))
#
# bmi = user_weight / user_height2
# print("Your double height is " + str(user_height2))
# print(bmi)
