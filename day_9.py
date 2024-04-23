import os


def clear_console():
    # Clear console command for Windows, Linux, and MacOS
    os.system("cls" if os.name == "nt" else "clear")


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def calculator():
    operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
    first_number = float(input("What is your first number? : "))
    continue_with_prev_result = ""

    while continue_with_prev_result != "n":
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the line above : ")
        second_number = float(input("What is your next number? : "))
        temp_first_num = first_number
        first_number = operations[operation_symbol](first_number, second_number)

        print(f"{temp_first_num} {operation_symbol} {second_number} = {first_number}")
        continue_with_prev_result = input(
            f"Type 'y' to continue with {first_number}, type 'n' to start new calculation or type 'c' to cancel out : "
        )
        if continue_with_prev_result == "c":
            return

    if continue_with_prev_result == "n":
        clear_console()
        calculator()


calculator()
