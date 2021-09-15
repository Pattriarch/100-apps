from art import logo
from random import choice
start = True

def play_game():
        print(logo)
        print("Welcome to the game 'Hot or cold'")
        print("I'm thinking number between 1 and 100")
        print("If you want to read rules, type 'rules' in choosing difficulty")
        difficulty = input("Choose a difficulty. Type 'easy', 'hard, 'pro' or 'god': ")

        def any_dif(attempts):
            number = choice(range(1, 100))
            game_is_running = True
            while game_is_running and attempts > 0:
                print(f"You have {attempts} attempts reamining to guees "
                  f"the number.")
                guess = int(input('Make a guess: '))
                if guess == number:
                    return print(f"Number is {number}. You won!")
                elif attempts > 0:
                    if abs(guess - number) > 60:
                        print('Very cold.')
                    elif 60 >= abs(guess - number) >= 20 :
                        print('Cold.')
                    elif 20 > abs(guess - number) >= 10:
                        print('Warm...')
                    elif 10 > abs(guess - number) >= 5:
                        print('Really warm!')
                    elif 5 > abs(guess - number) >= 4:
                        print('Ooh, hot!')
                    elif 3 > abs(guess - number) >= 2:
                        print('Hot! hot!')
                    else:
                        print('Ooh, on fire!!!')
                    attempts -= 1
                    if attempts > 0:
                        print("Guess again.")
            return print(f'You lose. Number is {number}')

        def game_rules():
            print('In this game, the computer randomly chooses a number from 1 to 100. '
                  'Your task is to guess the number given by the computer. The designations'
                  ' that the computer writes work like this: ')
            print("if your guess is more / less than the planned number by 60, then "
                  "the computer writes 'Very cold.''")
            print("                                                    ->  20-60,"
                  " then the computer writes 'Cold.'")
            print("                                                    ->  10-20,"
                  " then the computer writes 'Warm...'")
            print("                                                    ->  5-10,"
                  " then the computer writes 'Really warm!'")
            print("                                                    ->  4-5,"
                  " then the computer writes 'Ooh, hot!'")
            print("                                                    ->  2-3,"
                  " then the computer writes 'Hot! hot!'")
            print("                                                    ->  1,"
                  " then the computer writes 'Ooh, on fire!!!'")
            game = input("If you read rules and want to start game, then type 'start': ")
            if game == 'start':
                play_game()
            else:
                game_rules()


        if difficulty == 'easy':
            any_dif(10)
        elif difficulty == 'hard':
            any_dif(5)
        elif difficulty == 'pro':
            any_dif(3)
        elif difficulty == 'god':
            any_dif(2)
        elif difficulty == 'rules':
            game_rules()

        while input("Do you want to play more? Type 'yes' or 'no': ") == 'yes':
            play_game()
        print('Exit from game.')

while start:
    play_game()
    start = False