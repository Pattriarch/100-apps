from art import logo
from art import vs
from game_data import data
from random import choice


def not_identic(A, B):
    while A == B:
        A = choice(data)


Compaire_A = choice(data)
Compaire_B = choice(data)
not_identic(Compaire_A, Compaire_B)
game = True
score = 0
print(logo)

def compare(choose):
    if choose.lower() == 'a':
        if Compaire_A['follower_count'] > Compaire_B['follower_count']:
            return True
        else:
            return False
    elif choose.lower() == 'b':
        if Compaire_B['follower_count'] > Compaire_A['follower_count']:
            return True
        else:
            return False


def format(Compaire):
    return f"{Compaire['name']}, a {Compaire['description']}, from {Compaire['country']}"


while game:
    Compaire_A = Compaire_B
    Compaire_B = choice(data)
    print(f"Compaire A: {format(Compaire_A)}")
    print(vs)
    print(f"Compaire A: {format(Compaire_B)}")

    Choose = input("Who has more followers? Type 'A' or 'B': ").lower()
    result = compare(Choose)

    if result == True and Choose == 'a'.lower():
        score += 1
        print(f"Your current score = {score}")

    elif result == True and Choose == 'b'.lower():
        score += 1
        print(f"You current score = {score}")

    else:
        print('You lost!')
        print(f"You final score = {score}")
        game = False
