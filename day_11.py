from random import randint
from utils import clear_console

def guess_a_number():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    
    difficulty_lave = input("Chose a difficulty. Type 'easy' or 'hard': ")
    attempts = 10 if difficulty_lave == "easy" else 5
    number = randint(1, 100)
    highest = number + 5
    lowest = number - 5
    guesses = []

    while attempts != 0:
        guess = int(input("Make a guess: "))
        if guess == number:
            print("Congelation you win. You have a good guessing sense. the number was", number)
            return print("The number was", number)
        else:
            attempts -= 1
            guesses.append(guess)
            clear_console()

            if highest < guess:
                print(f"The number {guess} is too high")
            elif lowest > guess:
                print(f"The number {guess} is too low")
            elif highest > guess and lowest < guess:
                print("The number is in between")

            print(f"You have {attempts} attempts remaining to guess the number.")
            print("Your guesses", guesses)
            if attempts:
                print("Guess agin")

    print("The number was", number)

guess_a_number()