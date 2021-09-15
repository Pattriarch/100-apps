import random
from art import logo

first_game = True


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if len(cards) == 2 and sum(cards) == 21:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(us_score, comp_score):
    if us_score == comp_score:
        print("It's draw.")
    elif comp_score == 0:
        print("Comp got blackjack, you lose.")
    elif us_score == 0:
        print("Blackjack! You win.")
    elif us_score > comp_score > 21:
        print('You win.')
    elif comp_score > us_score > 21:
        print('Computer win.')
    elif us_score > 21:
        print('You lose.')
    elif comp_score > 21:
        print('You win.')
    elif us_score > comp_score:
        print('You win.')
    else:
        print('You lose.')


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    user_playing = True
    user_score = 0
    computer_score = 0

    for _ in range(2):
        user_card = deal_card()
        user_cards.append(user_card)
        computer_card = deal_card()
        computer_cards.append(computer_card)

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score {user_score}")
        print(f"Computer first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card or type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"You final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    compare(user_score, computer_score)

while input("Do you want to play a game of Blackjack? Type 'y' to play more or 'n' if no: ") == 'y':
    play_game()

