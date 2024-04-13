def brand_name_generator():
    print("Welcome to the band name generator!")
    city_name = input("What's the name of the cit you grew up in?\n")
    pets_name = input("What's your pet's name?\n")
    return f"Your band name could be {city_name} {pets_name}"


# print(brand_name_generator())


class TipCalculator:
    @staticmethod
    def calculate_tip():
        print("Welcome to the tip calculator.")

        total_bill = TipCalculator.convert_to_num(input("What was the total bill? $"))
        tip = TipCalculator.convert_to_num(input("What percentage tip would you like to give? 10, 12, or 15? "))
        num_people_to_split_bill = TipCalculator.convert_to_num(input("How many people to split the bill? "))

        bill_per_person = (total_bill + (total_bill * tip) / 100) / num_people_to_split_bill
        print(f"Each person should pay: {bill_per_person:.2f}")

    @staticmethod
    def convert_to_num(inp_str):
        try:
            return round(float(inp_str), 2)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            return 0.0


TipCalculator.calculate_tip()


def add_number():
    nums_str = input("Please enter an Integer: ")
    try:
        nums = int(nums_str)
        if nums <= 0:
            return "Number must be granter then 0"
    except ValueError:
        return "Invalid Number. Number must be an integer"
    result = 0
    for num in nums_str:
        result += int(num)
    return result


# print(add_number())

def convert_to_num(num_str, parse_type="int"):
    nums = 0
    try:
        if parse_type == "int":
            nums = int(num_str)
        elif parse_type == "float":
            nums = float(num_str)
        if nums <= 0:
            return "Number must be granter then 0"
    except ValueError:
        if parse_type == "int":
            return "Invalid Number. Number must be an integer"
        elif parse_type == "float":
            return "Invalid Number"
    return nums


def bmi_calculator():
    print("Welcome to BMI Calculator!")

    weight = convert_to_num(input("Please enter your weight(kg): "), "float")
    if not isinstance(weight, float):
        return weight

    height = convert_to_num(input("Please enter your height(m): "), "float")
    if not isinstance(height, float):
        return height

    return f"Your Body Mass Index(BMI) is: {round((weight / height ** 2), 2)}"


# print(bmi_calculator())

def calculate_num_of_weeks_left():
    age = convert_to_num(input("Please enter your age: "), "int")
    if not isinstance(age, int):
        return age

    num_of_year = 90
    average_weeks_par_year = 52
    total_weeks = num_of_year * average_weeks_par_year
    weeks_left = total_weeks - age * average_weeks_par_year

    return f"You have {weeks_left} weeks left."

# print(calculate_num_of_weeks_left())
