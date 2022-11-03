message2 = ''

reade_file = open('/home/kha1ide/PycharmProjects/100DaysPythonTut/01tut/day 8/sample.txt', 'r')
lines = reade_file.readlines()
for line in lines:
    for letter in line:
        print(letter)
        message2 += letter

reade_file.close()

print(message2)