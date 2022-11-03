import random

new_array = ["ghost", "paranoid", "confused", "lost"]

chosen_word = new_array[1]
# print(chosen_word)

# letter = 'o'
num = 0

print(chosen_word)

for letter in chosen_word:
    if letter == "a":
        num += 1

print(num)

