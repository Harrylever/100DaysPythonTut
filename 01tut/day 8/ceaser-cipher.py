small_Letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]

print(small_Letters[-26])
print(small_Letters[-97 % len(small_Letters)])
# print()

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# hkvek
# mfqaf mjqqt

# def encrypt(plain_text, shift_amount):
#     encrypt_word = ''
#     for i in plain_text:
#         i_index = small_Letters.index(i)
#         new_i_index = i_index + shift_amount
#         if new_i_index > len(small_Letters):
#             new_i_index = new_i_index % len(small_Letters)
#         encrypt_word += small_Letters[new_i_index]
#     print(f":: {encrypt_word} ::")
#
#
# def decrypt(cipher_text, shift_amount):
#     decrypt_word = ''
#     for i in cipher_text:
#         i_index = small_Letters.index(i)
#         new_i_index = i_index - shift_amount
#         decrypt_word += small_Letters[new_i_index]
#     print(f":: {decrypt_word} ::")


def caesar(message, shift_amount):
    new_i_index = 0
    word = ''
    for i in message:
        if i == " ":
            word += " "
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
                print(f"{new_i_index} = {i_index} - {shift_amount}")
            word += small_Letters[new_i_index]
    print(f":: {word} ::")

# def caesar(start_text, shift_amount, cipher_direction):
#     end_text = ""
#     shift_amount_ = 0
#     for letter in start_text:
#         # shift_amount = shift_amount
#         position = small_Letters.index(letter)
#         if cipher_direction == "decode":
#             shift_amount_ = shift_amount * -1
#         else:
#             shift_amount_ = shift_amount
#         new_position = position + shift_amount_
#         print(f"{new_position} = {position} + {shift_amount_}")
#         end_text += small_Letters[new_position]
#     print(f"Here's the {direction}d result: {end_text}")


# caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

caesar(message=text, shift_amount=shift)

# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)

# print(small_Letters)
# print(small_Letters[-1])
# print(len(small_Letters))
