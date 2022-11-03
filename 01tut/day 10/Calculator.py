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

num1 = float(input("What's the first number?: "))

print("Which operation do you want to carry out?:")
for operation in operations:
    print(operation)
operation_symbol = input("Enter operation: ")

num2 = float(input("What's the second number?: "))

function_ = operations[operation_symbol]
result = function_(num1, num2)
print_message = f"{round(num1)} {operation_symbol} {num2} = {result}"
print(print_message)

new_result = 0
while True:
    if new_result == 0:
        player_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit: ").lower()
    else:
        result = new_result
        player_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit: ").lower()
    if player_continue == "n":
        sys.exit()
    operation_symbol = input("Pick another operation: ")
    another_num = float(input("What's the next number?: "))
    function_ = operations[operation_symbol]
    new_result = function_(result, another_num)
    print_message = f"{round(result)} {operation_symbol} {another_num} = {new_result}"
    print(print_message)
