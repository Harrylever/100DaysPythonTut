total_bill = float(input("How much is the complete bill? $"))
print(f"The total bill is ${total_bill}")
percentage_tip = int(input("how much percentage tip do you want to pay? 10, 12, 15: "))
print(f"You are paying a {percentage_tip}% tip")
cut_amount = total_bill + (total_bill * (percentage_tip / 100))
noOfBilled = int(input("How many people are sharing the Bill? "))
# Round_up = str(round(cut_amount / noOfBilled, 2))
Round_up = "{:.2f}".format(cut_amount / noOfBilled)
print("Each person is paying $" + Round_up)
