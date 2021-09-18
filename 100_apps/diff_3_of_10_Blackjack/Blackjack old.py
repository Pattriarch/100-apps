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


def game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    user_playing = True

    for _ in range(2):
        user_card = deal_card()
        user_cards.append(user_card)
        computer_card = deal_card()
        computer_cards.append(computer_card)

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score {user_score}")
    print(f"Computer first card: {computer_cards[0]}")

    while not is_game_over:
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True

        while user_playing:
            if user_score < 21:
                question = input("Do you want to draw another card? Type 'yes' or 'no': ")
                if question == 'yes':
                    user_card = deal_card()
                    user_cards.append(user_card)
                    user_score = calculate_score(user_cards)
                    print(f"Your cards: {user_cards}, current score {user_score}")
                    print(f"Computer first card: {computer_cards[0]}")
                elif question == 'no':
                    user_playing = False
                else:
                    user_playing = False
            else:
                user_playing = False

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        print(f"Computer cards: {computer_cards} and score = {computer_score}")

        if computer_score < 17:
            print("Computer takes new card...")
            computer_card = deal_card()
            computer_cards.append(computer_card)
            computer_score = calculate_score(computer_cards)
        else:
            is_game_over = True

    compare(user_score, computer_score)

    print()
    ask = input("Do you want to continue playing blackjack? Type 'yes' or 'no': ")

    if ask == 'yes':
        game()
    else:
        print('Okay, goodbye!')


if first_game:
    game()
    first_game = False
