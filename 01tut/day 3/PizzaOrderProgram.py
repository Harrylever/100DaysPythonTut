print("Hello, Thanks for using Helon'D pizza delivery!")
bill = 0
print(f"Your bill current bill is ${bill}")
print("We have 3 different Pizza available\n1. Small Pizza: $15\n2. Medium Pizza: $20\n3. Large Pizza: $25")
print("=====================================================================")
print("=====================================================================")
print("======11=============22============3333==============================")
print("====1=11==========22===22==============33============================")
print("======11==============22===========3333==============================")
print("======11===========22==================33============================")
print("====111111========2222222==========3333==============================")
print("=====================================================================")
print("=====================================================================")

while True:
    chosen_pizza = input("Enter '1' for Pizza 1, '2' for Pizza 2, '3' for Pizza 3: ")
    # Chosen Pizza = 1
    if chosen_pizza == "1":
        bill += 15
        print(f"Your bill current bill is ${bill}")
        add_pepperoni = input("Do you want pepperoni? 'Y' or 'N': ")
        if add_pepperoni == "Y" or add_pepperoni == "y":
            bill += 2
            print(f"Your bill current bill is ${bill}")
        elif add_pepperoni == "N" or add_pepperoni == "n":
            bill += 0
            print(f"Your bill current bill is ${bill}")
        else:
            bill += 0
            print("Okay.")
            print(f"Your current bill for Pizza {chosen_pizza} is ${bill}")
        extra_cheese = input("Do you want Extra Cheese? 'Y' or 'N': ")
        if extra_cheese == "Y" or extra_cheese == "y":
            bill += 1
            print(f"Your final bill is ${bill}")
            break
        else:
            print("Okay.")
            print(f"Your final bill is ${bill}")
            break
    # Chosen Pizza = 2
    elif chosen_pizza == "2":
        bill += 20
        print(f"Your bill current bill is ${bill}")
        add_pepperoni = input("Do you want pepperoni? 'Y' or 'N': ")
        # if add_pepperoni == "Y" or add_personal == "y"
        # if add_pepperoni == ("Y" or "y"):
        if add_pepperoni == "Y" or add_pepperoni == "y":
            bill += 3
            print(f"Your current bill for Pizza {chosen_pizza} is ${bill}")
        elif add_pepperoni == "N" or add_pepperoni == "n":
            bill += 0
            print(f"Your current bill for Pizza {chosen_pizza} is ${bill}")
        else:
            bill += 0
            print("Okay.")
            print(f"Your current bill for Pizza {chosen_pizza} is ${bill}")
        extra_cheese = input("Do you want Extra Cheese? 'Y' or 'N': ")
        if extra_cheese == "Y" or extra_cheese == "y":
            bill += 1
            print(f"Your final bill for Pizza {chosen_pizza} is ${bill}")
            break
        else:
            print("Okay.")
            break
    # Chosen Pizza = 3
    elif chosen_pizza == "3":
        bill += 25
        print(f"Your bill current bill is ${bill}")
        add_pepperoni = input("Do you want pepperoni? 'Y' or 'N': ")
        if add_pepperoni == "Y" or add_pepperoni == "y":
            bill += 3
            print(f"Your current bill for Pizza {chosen_pizza} is ${bill}")
        elif add_pepperoni == "N" or add_pepperoni == "n":
            bill += 0
            print(f"Your current bill for Pizza {chosen_pizza} is ${bill}")
        else:
            print("Okay.")
            print(f"Your current bill for Pizza {chosen_pizza} is ${bill}")
        extra_cheese = input("Do you want Extra Cheese? 'Y' or 'N': ")
        if extra_cheese == "Y" or extra_cheese == "y":
            bill += 1
            print(f"Your final bill for Pizza {chosen_pizza} is ${bill}")
            break
        else:
            print("Okay.")
            print(f"Your final bill for Pizza {chosen_pizza} is ${bill}")
            break
    else:
        print("Please choose enter either '1', '2' or '3'.")
