def odd_or_even():
    num = int(input("Please enter a number: "))
    if not isinstance(num, int):
        return "Please enter a Integer number"
    if num % 2:
        print(f"{num} Is an Odd Number")
    else:
        print(f"{num} Is an Even Number")


# odd_or_even()


def validate_ride():
    print("Welcome to the roller-coaster!")
    height = int(input("What is your height in cm? "))

    if height >= 120:
        age = int(input("What is your age? "))
        print(
            f"You can ride the roller-coaster! And your ticket would be {'5' if age < 12 else '7' if 12 <= age <= 18 else '12'}$")
    else:
        print("Sorry, you have to grow taller before you can ride.")


# validate_ride()


def check_guest_list():
    guest_list = {"saiful", "delo", "shovo", "nayan"}
    guest_name = input("Please enter your you name: ")

    if guest_name.strip().lower() in guest_list:
        print(f"Welcome {guest_name}! Enjoy the party!")
    else:
        print("Sorry your name is not on the lease. Better next time.")


# check_guest_list()


def python_pizza():
    print("Welcome to Python Pizza!")
    size = input("What size do you want S, M or L : ").strip().lower()
    add_pepperoni = input("Do you want pepperoni? Y or N : ").strip().lower()
    extra_cheese = input("Do you want extra cheese? Y or N : ").strip().lower()

    price_table = {
        "s": {"price": 15, "pepperoni": 2, "cheese": 1},
        "m": {"price": 20, "pepperoni": 3, "cheese": 1},
        "l": {"price": 25, "pepperoni": 3, "cheese": 1},
    }

    pizza_details = price_table.get(size)
    bill = pizza_details["price"]

    if add_pepperoni == "y":
        bill += pizza_details["pepperoni"]
    if extra_cheese == "y":
        bill += pizza_details["cheese"]

    print("Thank you for choosing Python Pizza Deliveries!")
    print(f"Your final bill is ${bill}")


# python_pizza()

pi = 3.1416
