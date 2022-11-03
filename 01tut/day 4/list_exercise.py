import random

names_string = input("Give me everybody's names, separated by a comma:\n")
names_list = names_string.split(",")

# print(type(names_list))
# print(names_list)

names_length = len(names_list)
selected_name = random.randint(0, names_length - 1)
message = f"{names_list[selected_name]} is going to pay the bill"
print(message)
