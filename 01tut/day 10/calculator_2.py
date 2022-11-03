# Add Function
import sys


def add(n1, n2):
    """Add two numbers"""
    return n1 + n2


# Subtract Function
def subtract(n1, n2):
    """Subtract two numbers"""
    return n1 - n2


# Multiply
def multiply(n1, n2):
    """Multiply two numbers"""
    return n1 * n2


# Divide
def divide(n1, n2):
    """Divide two numbers"""
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    num1 = float(input("What's the first number?: "))
    for operation in operations:
        print(operation)
    should_continue = True

    while should_continue:
        operation_symbol = input("Enter operation: ")
        num2 = float(input("What's the second number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"\n:: {round(num1)} {operation_symbol} {num2} = {answer} ::\n")

        player_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation or type 'exit' to exit calculator: ").lower()
        if player_continue == "y":
            num1 = answer
        elif player_continue == "exit":
            print("Goodbye...")
            sys.exit()
        else:
            should_continue = False
            calculator()


calculator()
