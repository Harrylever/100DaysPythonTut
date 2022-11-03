userAge = input("How old are you? ")

agesLeft = 90 - int(userAge)
currentYear = 2022
noOfDaysInYear = 365
noOfDaysLeft = noOfDaysInYear * agesLeft
noOfWeeksInYear = 52
noOfWeeksLeft = noOfWeeksInYear * agesLeft
noOfMonthsInYear = 12
noOfMonthsLeft = noOfMonthsInYear * agesLeft
# deathYear = currentYear + agesLeft
# print(deathYear)

days = noOfDaysLeft
weeks = noOfWeeksLeft
months = noOfMonthsLeft

print(f"You have {days} days, {weeks} weeks, and {months} months left")
