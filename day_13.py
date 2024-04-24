def calculate_total():
    COIN_VALUES = {"penny": 0.01, "nickel": 0.05, "dime": 0.10, "quarter": 0.25}

    quarter = float(input("How many quarters? : ")) * COIN_VALUES["quarter"]
    dime = float(input("How many dimes? : ")) * COIN_VALUES["dime"]
    nickel = float(input("How many nickles? : ")) * COIN_VALUES["nickel"]
    penny = float(input("How many pennies? : ")) * COIN_VALUES["penny"]

    return quarter + dime + nickel + penny


def is_resource_sufficient(order_ingredients, coffee_resources):
    for key in order_ingredients:
        if not key == "price":
            if order_ingredients[key] == coffee_resources[key]:
                continue
            elif order_ingredients[key] > coffee_resources[key]:
                print("Sorry there is not enough", key)
                return False
    return True

def coffee_maker():
    MENU = {
        "espresso": {
            "price": 1.5,
            "water": 50,
            "coffee": 18,
        },
        "latte": {
            "price": 2.5,
            "water": 200,
            "coffee": 24,
            "milk": 150,
        },
        "cappuccino": {
            "price": 3,
            "water": 250,
            "coffee": 24,
            "milk": 100,
        },
    }
    coffee_resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}

    while True:
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if user_input == "power off":
            return print("Power off")

        if user_input == "report":
            print(
                f"""Water: {coffee_resources["water"]}ml \nMilk: {coffee_resources["milk"]}ml \nCoffee: {coffee_resources["coffee"]}g \nMoney: ${coffee_resources["money"]}"""
            )
        else:
            user_chosen_coffee = MENU[user_input]

            print(f"Your {user_input} would be {user_chosen_coffee['price']}$")
            print("Please insert coins.")

            # calculate_total f is taking care of input and getting money.
            total = calculate_total()
            
            if user_chosen_coffee["price"] > total:
                print("Sorry that's not enough money. Money refunded.")
            else:
                if is_resource_sufficient(user_chosen_coffee, coffee_resources):
                    change = total - user_chosen_coffee["price"]
                    (
                        print(f"Here is your ${round(change, 2)} change.")
                        if not change <= 0
                        else None
                    )
                    print(f"Here is your {user_input} Enjoy!")

                    for key in user_chosen_coffee:
                        if key == "price":
                            coffee_resources["money"] = (
                                coffee_resources["money"] + user_chosen_coffee[key]
                            )
                        else:
                            coffee_resources[key] = (
                                coffee_resources[key] - user_chosen_coffee[key]
                            )


coffee_maker()
