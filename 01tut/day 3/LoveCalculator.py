print("welcome to the Love Calculator")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

combined_name = name1 + name2
# print(combined_name.count("t"))
# true

var_t = combined_name.count("t")
var_r = combined_name.count("r")
var_u = combined_name.count("u")
var_e = combined_name.count("e")

added_true = var_t + var_r + var_u + var_e
# print(added_true)
# print("=+" * 30)
# print("")
# love
var_l = combined_name.count("l")
var_o = combined_name.count("o")
var_v = combined_name.count("v")
var_e2 = combined_name.count("e")
added_love = var_l + var_o + var_v + var_e2
# print(added_love)
# print("=+" * 30)
# print("")

combined_name_number = str(added_true) + str(added_love)
combined_name_number_int = int(combined_name_number)

if combined_name_number_int < 10 or 90 < combined_name_number_int:
    print(f"Your score is {combined_name_number}, you go together like Coke and Mentos.")
elif 40 < combined_name_number_int < 50:
    print(f"Your score is {combined_name_number}, you are alright together.")
else:
    print(f"Your score is {combined_name_number}.")
# print(combined_name_number + "\n")
