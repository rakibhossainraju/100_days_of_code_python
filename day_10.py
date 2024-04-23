# Black Jack
from random import choice


def deal_card(cards = []):
    card = choice(cards)
    cards.remove(card)
    print(len(cards))
    return card


def calculate_score(cards=[]):
    total = sum(
        (
            11
            if isinstance(card, str) and card == "a"
            else 10 if isinstance(card, str) else card
        )
        for card in cards
    )

    if total == 21 and len(cards) == 2:
        return 0
    if total > 21 and "a" in cards:
        return sum(
            (
                1
                if isinstance(card, str) and card == "a"
                else 10 if isinstance(card, str) else card
            )
            for card in cards
        )
    return total

def compare(users_score, computers_score):
    if users_score == computers_score:
        return "It's a draw"
    if not users_score:
        return "You win"
    if not computers_score:
        return "You lose"
    if users_score > 21:
        return "You went over. you lose"
    if computers_score > 21:
        return "Computer went over you win"
    if users_score > computers_score:
        return "You win"
    return "You lose"

def black_jack():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "j", "k", "q"]
    users_cards = [deal_card(cards), deal_card(cards)]
    computers_cards = [deal_card(cards), deal_card(cards)]
    is_game_over = False

    users_score = calculate_score(users_cards)
    computers_score = calculate_score(computers_cards)



    while not is_game_over:
        print("Your cards:", users_cards, "Your current total: ", 21 if not users_score else users_score )
        print("Computer's first card:", computers_cards[0])
        if users_score == 0  or computers_score == 0 or users_score > 21  or computers_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                users_cards.append(deal_card(cards))
                users_score = calculate_score(users_cards)   
            else:
                is_game_over = True

    while computers_score != 0 and computers_score < 19:
        computers_cards.append(deal_card(cards))
        computers_score = calculate_score(computers_cards)           
    
    print("Your final hand", users_cards, "Total score", 21 if not users_score else users_score )
    print("Computers final hand", computers_cards, "Total score", 21 if not computers_score else computers_score)
    print(compare(users_score, computers_score))


black_jack()
