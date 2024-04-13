import os
import random


def clear_console():
    # Clear console command for Windows, Linux, and MacOS
    os.system('cls' if os.name == 'nt' else 'clear')


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''


def hangman():
    life = 6
    word_list = ["banana", "cake", "egge", "mobile"]
    chosen_word = word_list[random.randint(0, 3)]
    display = ["_"] * len(chosen_word)
    guessed_one_wrong = False

    print(logo, "\n")

    while life >= 1:
        if chosen_word == "".join(display):
            print("Congratulation you won the word was", chosen_word)
            return
        guess = input("Guess a letter of the word: ").lower()
        clear_console()

        guessed_correctly = False

        if guess in display:
            print(f"You've already guessed {guess}")

        for i in range(len(chosen_word)):
            if guess == chosen_word[i]:
                display[i] = guess
                guessed_correctly = True
        if not guessed_correctly:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            guessed_one_wrong = True
            life -= 1
        if guessed_one_wrong:
            print(stages[life])
        print(" ".join(display), "\n")
    print("You lose the game")


hangman()
