import random

number_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
small_Letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
capital_Letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
letters = [capital_Letters, small_Letters]

print("Welcome to the PyPassword Generator!")
nr_capital_letters = int(input("How many capital letters would you like in your password?\n: "))
nr_small_letters = int(input("How many small letters would you like in your password?\n: "))
nr_symbols = int(input("How many symbols would you like?\n: "))
nr_numbers = int(input("How many numbers would you like?\n: "))

# user_password = ""

# for char in range(1, nr_capital_letters + 1):
#     user_password += random.choice(capital_Letters)
#
# for char in range(1, nr_small_letters + 1):
#     user_password += random.choice(small_Letters)
#
# for char in range(1, nr_symbols + 1):
#     user_password += random.choice(symbols)
#
# for char in range(1, nr_numbers + 1):
#     user_password += random.choice(number_list)

user_password = []

for char in range(1, nr_capital_letters + 1):
    user_password.append(random.choice(capital_Letters))

for char in range(1, nr_small_letters + 1):
    user_password += random.choice(small_Letters)

for char in range(1, nr_symbols + 1):
    user_password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    user_password += random.choice(number_list)

# print(user_password)
random.shuffle(user_password)

password = ""
for char in user_password:
    password += char

passwordDetail = input("What account is the password for? e.g. Instagram, Facebook, Twitch: ")
passwordUsername = input("What is the username of the password: ")

password_text = "Your Password for username '" + passwordUsername + "' on " + passwordDetail + " is '" + password + "'."
print(password_text)

password_file = open('/home/kha1ide/Resources/Notes/.Passwords/passwords.txt', 'a')
# password_file = open("/home/kha1ide/Resources/.Passwords/passwords.txt", 'a')


print(password_text, file=password_file)

password_file.close()
