# ##################################DEBUGGING############################################

# # Describe the problem
# def my_function():
#     for i in range(1, 20):
#         print(i)
#
#
# my_function()


# # Reproduce the bug
# from random import randint
# dice_imgs = ["1", "2", "3", "4", "5", "6"]
# dice_num = randint(0, 5)
# print(dice_num)
# print(dice_imgs[dice_num])


# # Play Computer
# year = int(input("What is your year of birth?: "))
# if 1980 < year < 1994:
#     print("You are a millennial.")
# elif year >= 1994:
#     print("Your a Gen Z.")


# # Fix the Errors
# age = int(input("How old are you?: "))
# if age > 18:
#     print(f"You can drive at age {age}.")


# Print is your friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of Pages: "))
# # word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)


# Using a Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
