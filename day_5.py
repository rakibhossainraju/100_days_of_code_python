import random


def sum_of_even():
    target = int(input("Enter a number between 0 and 100: "))
    total = 0
    for num in range(2, target + 1, 2):
        total += num
        print(num)
    print("Total", total)


# sum_of_even()


def fizz_buzz():
    output = []
    target = int(input("Enter a number between 0 and 100: "))
    for num in range(1, target + 1):
        if not num % 3 and not num % 5:
            output.append("Fizz-Buzz")
        elif not num % 3:
            output.append("Fizz")
        elif not num % 5:
            output.append("Buzz")
        else:
            output.append(num)
    print(output)


# fizz_buzz()

def get_random_int(a, b):
    return random.randint(a, b)


def py_password_generator():
    print("Welcome to the PyPassword Generator!")
    small_letters = (97, 122)  # ASCII values for lowercase letters 'a' to 'z'
    capital_letters = (65, 90)  # ASCII values for uppercase letters 'A' to 'Z'
    numbers = (48, 57)  # ASCII values for numbers '0' to '9'
    symbols = ((33, 47), (58, 64), (91, 96), (123, 126))  # ASCII values for symbols

    try:
        letter_in_pass = int(input("How many letters would you like in your password_list?\n"))
        symbols_in_pass = int(input("How many symbols would you like in your password_list?\n"))
        numbers_in_pass = int(input("How many numbers would you like in your password_list?\n"))
    except ValueError:
        return print("Please enter a positive integer as the input")

    password_list = []

    for __ in range(0, letter_in_pass):
        if get_random_int(0, 1):
            password_list.append(chr(get_random_int(small_letters[0], small_letters[1])))
        else:
            password_list.append(chr(get_random_int(capital_letters[0], capital_letters[1])))

    for __ in range(0, numbers_in_pass):
        password_list.append(chr(get_random_int(numbers[0], numbers[1])))

    for __ in range(0, symbols_in_pass):
        random_symbol = symbols[get_random_int(0, len(symbols) - 1)]
        password_list.append(chr(get_random_int(
            random_symbol[0],
            random_symbol[1]
        )))

    random.shuffle(password_list)
    password_str = "".join(password_list)
    print("Your strong password is:", password_str)


py_password_generator()
