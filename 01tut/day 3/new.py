print("Welcome to the RollerCoaster!")

height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age? "))
    if age == 12:
        bill += 5
        print("Children tickets are $5.")
    # elif age <= 18:
    #     bill += 7
    #     print("Youth tickets are $7.")
    else:
        bill += 12
        print("Adult tickets are $12.")
    print(bill)
    photo_state = input("Do you want a picture taken? Y or N: ")
    if photo_state == "Y" or "y":
        # Add $3 to the bill
        bill += 3
    elif photo_state == "N" or "n":
        print("Fuck You")

    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can take this ride.")
