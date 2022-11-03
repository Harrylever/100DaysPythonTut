import random

# chosen_word = []
word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(f'this is {chosen_word}')

display = []
for i in range(len(chosen_word)):
    display += "_"

num = len(display)

print(num)

while num > 0:
    for letter in display:
        if letter != "_":
            num -= 1

    guess = input("Guess a letter: ").lower()

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = chosen_word[i]
            # else:
            # print("Wrong")

    print(display)
    print(num)
    # for letter in chosen_word:
    #     if letter == guess:
    #         print("Right")
    #     else:
    #         print("Wrong")
