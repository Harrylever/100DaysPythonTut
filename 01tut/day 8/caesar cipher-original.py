import sys

small_Letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]

while True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    def caesar(message, shift_amount):
        new_i_index = 0
        word = ''
        for i in message:
            print(i)
            if i == " ":
                word += ""
            if i not in small_Letters:
                word += i
            elif i in small_Letters:
                i_index = small_Letters.index(i)
                if direction == "encode":
                    new_i_index = i_index + shift_amount
                    if new_i_index > len(small_Letters):
                        new_i_index = new_i_index % len(small_Letters)
                        print(new_i_index)
                elif direction == "decode":
                    new_i_index = i_index - shift_amount
                    if new_i_index < -len(small_Letters):
                        # print("It is true")
                        new_i_index = new_i_index % len(small_Letters)
                    # print(f"{new_i_index} = {i_index} - {shift_amount}")
                word += small_Letters[new_i_index]
        print(f":: {word} ::")


    caesar(message=text, shift_amount=shift)

    run_again = input("Restart the Cipher Program? \"Yes\" \"No\" ").lower()
    if run_again == "no":
        print("Goodbye..")
        sys.exit()
        # break
