from art import logo

print(logo)
print('Welcome to the secret auction program.')

flag = True
list_of_participants = {}

def find_highest_bidder():
    name_of_winner = ''
    max_bet = 0
    for i in list_of_participants:
        if list_of_participants[i] > max_bet:
            max_bet = list_of_participants[i]
            name_of_winner = i
    print(f'The winner of our action is {name_of_winner} with bid = ${max_bet}')

while flag == True:
    name = input('What is your name?:\n')
    bid = int(input('What\'s your bid?: $'))
    list_of_participants[name] = bid
    more = input("Are they any other bidders? Type 'yes' or 'no'.\n")
    if more == 'yes':
        pass
        for i in range(40):
            print()
    elif more == 'no':
        flag = False
        for i in range(40):
            print()
            find_highest_bidder()
    else:
        print("You've choose wrong statement!")
