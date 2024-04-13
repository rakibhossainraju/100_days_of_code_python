import random

welcome_message = '''
        $$\   $$\ $$$$$$$$\ $$\       $$\       $$$$$$\    
        $$ |  $$ |$$  _____|$$ |      $$ |     $$  __$$\   
        $$ |  $$ |$$ |      $$ |      $$ |     $$ /  $$ |  
        $$$$$$$$ |$$$$$\    $$ |      $$ |     $$ |  $$ |  
        $$  __$$ |$$  __|   $$ |      $$ |     $$ |  $$ |  
        $$ |  $$ |$$ |      $$ |      $$ |     $$ |  $$ |  
        $$ |  $$ |$$$$$$$$\ $$$$$$$$\ $$$$$$$$\ $$$$$$  |  
        \__|  \__|\________|\________|\________|\______/
        '''
rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''


def rock_paper_scissors():
    store = ["Rock", "Paper", "Scissors"]
    game_images = {"Rock": rock, "Paper": paper, "Scissors": scissors}
    computers_choice = store[random.randint(0, 2)]
    print(welcome_message, "Welcome to Rock Paper Scissors!")
    try:
        users_choice = store[int(input("What do you chose? Type 0 for Rock, 1 for Paper 2 for Scissors.\n"))]
    except IndexError:
        return print("Invalid input please enter a valid input ( 0, 1, 2 )")
    except ValueError:
        return print("Invalid input please enter a valid input ( 0, 1, 2 )")

    game_rules = {
        "Rock": {"wins": "Scissors", "looses": "Paper"},
        "Paper": {"wins": "Rock", "looses": "Scissors"},
        "Scissors": {"wins": "Paper", "looses": "Rock"}
    }

    print(f"You chose: \n", game_images[users_choice])
    print(f"Computer chose: \n", game_images[computers_choice])

    if users_choice is computers_choice:
        print("It's a draw")
    elif users_choice is game_rules[computers_choice]["looses"]:
        print(f"{users_choice} wins against {computers_choice} so you win")
    elif users_choice is game_rules[computers_choice]["wins"]:
        print(f"{users_choice} looses against {computers_choice} so you lose")


rock_paper_scissors()
