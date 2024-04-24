from typing import Union


class Drink:
    def __init__(
        self, name: str, price: float, water: int, coffee: int, milk: int = 0
    ) -> None:
        self.name = name
        self.price = price
        self.ingredients = {"water": water, "coffee": coffee, "milk": milk}


class Menu:
    def __init__(self) -> None:
        self.menu = [
            Drink(name="espresso", price=1.5, water=50, coffee=18),
            Drink(name="latte", price=2.5, water=100, coffee=24, milk=150),
            Drink(name="cappuccino", price=3, water=250, coffee=24, milk=200),
        ]

    def get_menu_items(self) -> str:
        options = ""
        for option in self.menu:
            options += option.name + "/"
        return options

    def find_drink(self, order_name: str) -> Union[Drink, None]:
        for drink in self.menu:
            if order_name == drink.name:
                return drink
                
        print("Sorry that item is not available.")
        return None


class MoneyMachine:
    def __init__(self) -> None:
        self.CURRENCY = "$"

        self.money = 0

        self.COIN_VALUES = {
            "quarter": 0.25,
            "dime": 0.10,
            "nickel": 0.05,
            "penny": 0.01,
        }

    def report(self) -> None:
        print(f"Money: {self.CURRENCY}{self.money}")

    def make_payment(self, price: float) -> bool:
        total = self.process_coins()

        if total >= price:
            self.money = self.money + price
            print(f"Here is your change {round(total - price, 2)}{self.CURRENCY}") if total - price > 0 else None
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False

    def process_coins(self) -> float:
        print("Please insert coins.")
        money_received = 0

        for coin in self.COIN_VALUES:
            money_received += (
                float(input(f"How many {coin}? : ")) * self.COIN_VALUES[coin]
            )
        return money_received


class CoffeeMaker:
    def __init__(self) -> None:
        self.water = 500
        self.milk = 500
        self.coffee = 200

    def report(self) -> None:
        print(f"Water: {self.water}ml")
        print(f"Milk: {self.milk}ml")
        print(f"Coffee: {self.coffee}g")

    def is_resource_sufficient(self, drink: Drink) -> bool:
        for key in drink.ingredients:
            if getattr(self, key) == drink.ingredients[key]:
                continue
            elif getattr(self, key) < drink.ingredients[key]:
                print(f"Sorry there is not enough {key}")
                return False

        for key in drink.ingredients:
            setattr(self, key, getattr(self, key) - drink.ingredients[key])

        return True


def make_coffee():
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()

    while True:
        user_choice = (
            input(f"What would you like to have today? ({menu.get_menu_items()}): ")
            .lower()
            .strip()
        )

        if user_choice == "power off":
            return print("Power off!")
        if user_choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            user_chosen_coffee = menu.find_drink(user_choice)

            if coffee_maker.is_resource_sufficient(user_chosen_coffee):
                print(
                    f"{user_choice.title()} is {user_chosen_coffee.price}{money_machine.CURRENCY}"
                )
                if money_machine.make_payment(user_chosen_coffee.price):
                    print(f"Here is your {user_choice}. Enjoy your coffee ☕☕☕!")

make_coffee()
