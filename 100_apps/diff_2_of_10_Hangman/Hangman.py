import random
from logo_and_stages import logo
from logo_and_stages import stages
from words import word_list

print(logo)
word = random.choice(word_list).lower()
print(word)
word_length = len(word)
end_of_game = False

print("Welcome to the hangman game!")

word_to_answer = []
for i in word:
    word_to_answer.append('_')

life_count = 6

container = []
q = False

while not end_of_game:
    guess = input('Guess a letter: ')
    if guess in container:
        print('You\'ve already choose this letter!')
        q = True
    else:
        container += guess
        q = False

    for position in range(word_length):
        letter = word[position]
        if letter == guess:
            word_to_answer[position] = letter

    if (guess not in word) and (q == False):
        life_count -= 1
        print('You\'ve choose wrong letter.')
        # print(stages[life_count])

    if life_count == 0:
        print('You lost all of your lives')
        end_of_game = True

    print(f"{' '.join(word_to_answer)}")

    print(stages[life_count])

    if '_' not in word_to_answer:
        end_of_game = True
        print('You won!')
        print(f'Word is:', word)
