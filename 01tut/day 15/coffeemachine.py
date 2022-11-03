from res import MENU, resources

game_resource_water = resources["water"]
game_resource_milk = resources["milk"]
game_resource_coffee = resources["coffee"]
game_resource_money = 0
payment = 0


def take_order():
    run_again = True
    while run_again:
        customer_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if customer_choice == "off":
            run_again = False
            print("Goodbye...")
            exit()
        elif customer_choice == "espresso":
            return "espresso"
        elif customer_choice == "latte":
            return "latte"
        elif customer_choice == "cappuccino":
            return "cappuccino"
        elif customer_choice == "report":
            print(f"Water: {game_resource_water}ml \nMilk: {game_resource_milk}ml \nCoffee: {game_resource_coffee}g \nMoney: ${game_resource_money}")
        else:
            print("Invalid input!")


def process_payment(order):
    global game_resource_money, payment, game_resource_water, game_resource_milk, game_resource_coffee
    available_resources_water = game_resource_water
    available_resources_milk = game_resource_milk
    available_resources_coffee = game_resource_coffee

    required_resource_water = MENU[order]["ingredients"]["water"]
    required_resource_milk = MENU[order]["ingredients"]["milk"]
    required_resource_coffee = MENU[order]["ingredients"]["coffee"]
    required_resource_cost = MENU[order]["cost"]

    if available_resources_water < required_resource_water:
        print("Sorry there is no enough water.")
        return
    elif available_resources_milk < required_resource_milk:
        print("Sorry there is no enough water.")
        return
    elif available_resources_coffee < required_resource_coffee:
        print("Sorry there is no enough coffee.")
        return

    retake_payment = True
    while retake_payment:
        print("Please insert coins.")
        no_of_quarters = int(input("How many quarters?: "))
        no_of_dimes = int(input("How many quarters?: "))
        no_of_nickles = int(input("How many quarters?: "))
        no_of_pennies = int(input("How many quarters?: "))

        total_payment_quarters = no_of_quarters * 0.25
        total_payment_dimes = no_of_dimes * 0.10
        total_payment_nickles = no_of_nickles * 0.05
        total_payment_pennies = no_of_pennies * 0.01
        total_payment = total_payment_pennies + total_payment_nickles + total_payment_dimes + total_payment_quarters

        if total_payment < required_resource_cost:
            print("Sorry that's not enough money. Money refunded.")
            return
            # come_back = input("Or would you come back later? Type 'Yes' or 'No': ").lower()
            # if come_back == "yes":
            #     exit()
        else:
            retake_payment = False
            if total_payment > required_resource_cost:
                payment_change = total_payment - required_resource_cost
                print(f"Here is ${round(payment_change, 2)} in change.")
            game_resource_money += required_resource_cost
            print(f"Here is your {order}. Enjoy!")

    game_resource_water -= required_resource_water
    game_resource_milk -= required_resource_milk
    game_resource_coffee -= required_resource_coffee


def run_coffee_machine():
    while True:
        order = take_order()
        process_payment(order=order)


run_coffee_machine()
