import random

choose = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
comp_peek = random.randint(0, 2)

rock = ("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

game_pictures = [rock, paper, scissors]

print(f'Your choice is:\n {game_pictures[choose]}')


def print_opponent_choice():
    print('Your opponent choice is:')
    print(game_pictures[comp_peek])


if choose == comp_peek:
    print_opponent_choice()
    print('It\'s a draw!')
elif (choose == 0) and (comp_peek == 2):
    print_opponent_choice()
    print('You won, congratulations!')
elif (choose == 2) and (comp_peek == 0):
    print_opponent_choice()
    print('You\'ve lost!')
elif choose > comp_peek:
    print_opponent_choice()
    print('You won, congratulations!')
elif choose < comp_peek:
    print_opponent_choice()
    print('You\'ve lost!')
else:
    print('You\'ve choose wrong number!')
