from random import choice
from art import logo

start = True
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def game():
    def set_difficulty():
        level = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if level == 'easy':
            return EASY_LEVEL_TURNS
        else:
            return HARD_LEVEL_TURNS


    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking a number between 1 and 100")
    attempts = set_difficulty()
    number = choice(range(1, 100))

    game_is_running = True
    while game_is_running and attempts > 0:
        print(f"You have {attempts} attempts remaining to guess "
          f"the number.")
        guess = int(input('Make a guess: '))
        if guess == number:
            return print(f"Number is {number}. You won!")
        elif attempts > 0:
            if guess > number:
                print('Too high.')
            else:
                print('Too low.')
            attempts -= 1
            if attempts > 0:
                print("Guess again.")
        else:
            return print(f'You lose. Number is {number}')

    print()
    next = input("Do you want to restart game? Type 'y' or 'n': ")
    if next == 'y':
        game()
    else:
        pass

if start:
    game()
    start = False