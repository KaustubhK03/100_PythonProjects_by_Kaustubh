import random
from art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over, you lose"
    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "You lost, the dealer has a blackjack"
    elif user_score == 0:
        return "You won, you have a blackjack"
    elif user_score > 21:
        return "You went over and lost!"
    elif computer_score > 21:
        return "Computer went over, you won!"
    elif user_score > computer_score:
        return "You won!"
    else:
        return "You lost!"


def play_game():
    print(logo)
    user_cards = []
    computers_cards = []
    for _ in range(2):
        user_cards.append(deal_card())
        computers_cards.append(deal_card())

    while True:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computers_cards)
        print(f"The user's cards are: {user_cards} and Score = {user_score}")
        print(f"The computer's first card = {computers_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            break

        new_card = input("Do you want another card? (y/n): ")
        if new_card.lower() == 'y':
            user_cards.append(deal_card())
        else:
            break

    while computer_score != 0 and computer_score < 17:
        computers_cards.append(deal_card())
        computer_score = calculate_score(computers_cards)

    print(f"Your final hand: {user_cards} and your final score = {user_score}")
    print(f"Computer's final hand: {computers_cards} and computer's final score = {computer_score}")
    print(compare(user_score, computer_score))

while True:
    play_game()
    if input("Do you want to play another game of Blackjack? Type 'y' or 'n': ").lower() != 'y':
        break