from random import choice
from art import logo

start = True
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_difficulty():
    level = input("Choose a difficulty. Type 'NG easy mode' or 'NG Hard Mode': ")
    if level == 'NG easy mode':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def check_answer(guess, number, attempts):
    if guess < number:
        print('Too low!')
        return attempts - 1
    if guess > number:
        print('Too high!')
        return attempts - 1
    else:
        return attempts


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking a number between 1 and 100")

    number = choice(range(1, 100))
    attempts = set_difficulty()

    guess = 0
    while guess != number:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts = check_answer(guess, number, attempts)

        if attempts == 0:
            print("You've run out guesses, you lose.")

    else:
        print(f"You've got it! It's {number}")


game()
