from random import choice
from art import logo

start = True

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking a number between 1 and 100")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    number = choice(range(1, 100))

    def guess_hard():
        game_is_running = True
        attempts = 5
        while game_is_running and attempts > 0:
            print(f"You have {attempts} attempts reamining to guees "
              f"the number.")
            guess = int(input('Make a guess: '))
            if guess == number:
                return print(f"Number is {number}. You won!")
            elif attempts > 0:
                if guess > number:
                    print('Too high.')
                else:
                    print('Too low.')
                print("Guess again.")
                attempts -= 1
        return print(f'You lose. Number is {number}')

    def guess_easy():
        game_is_running = True
        attempts = 10
        while game_is_running and attempts > 0:
            print(f"You have {attempts} attempts reamining to guees "
              f"the number.")
            guess = int(input('Make a guess: '))
            if guess == number:
                return print(f"Number is {number}. You won!")
            elif attempts > 0:
                if guess > number:
                    print('Too high.')
                else:
                    print('Too low.')
                print("Guess again.")
                attempts -= 1
        return print(f'You lose. Number is {number}')


    if difficulty.lower() == 'easy':
        guess_easy()
    elif difficulty.lower() == 'hard':
        guess_hard()
    else:
        print('Wrong difficulty!')
        game()

    print()
    next = input("Do you want to restart game? Type 'y' or 'n': ")
    if next == 'y':
        game()
    else:
        pass

if start:
    game()
    start = False