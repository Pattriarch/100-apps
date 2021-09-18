from art import logo
from art import vs
from game_data import data
from random import choice


def not_ident(a, b):
    while a == b:
        a = choice(data)


comp_a = choice(data)
comb_b = choice(data)
not_ident(comp_a, comb_b)
game = True
score = 0
print(logo)


def compare(choose):
    if choose.lower() == 'a':
        if comp_a['follower_count'] > comb_b['follower_count']:
            return True
        else:
            return False
    elif choose.lower() == 'b':
        if comb_b['follower_count'] > comp_a['follower_count']:
            return True
        else:
            return False


def value(compair):
    return f"{compair['name']}, a {compair['description']}, from {compair['country']}"


while game:
    comp_a = comb_b
    comb_b = choice(data)
    print(f"Compair A: {value(comp_a)}")
    print(vs)
    print(f"Compair A: {value(comb_b)}")

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
