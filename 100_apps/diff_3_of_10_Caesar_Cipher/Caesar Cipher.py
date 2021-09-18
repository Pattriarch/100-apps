from art import logo
import time

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# Function that encode and decode text
def caesar(simple_text, shift_amount, directions):
    cipher_text = ''
    act = -1
    # If direction is not encode, then we change shift amount and flag
    if directions == 'decode':
        shift_amount *= -1
        act = 1
    for letter in simple_text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            # Check every letter in alphabet
            for i, char in enumerate(alphabet):
                if letter == char:
                    # If index + shift amount less than length alphabet it's okay
                    if i + shift_amount < len(alphabet):
                        cipher_text += alphabet[i + shift_amount]
                    # If index + shift amount more than length alphabet, then we need to nullify our indexes
                    elif i + shift_amount > len(alphabet) - 1:
                        amount = i + shift_amount // 26
                        cipher_text += alphabet[i + amount * act * 26 + shift_amount]
    print(f'The {directions} word is: {cipher_text}')


# Flag was created to check if user wants to end program or restart her
flag = False
while not flag:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    # Two flags to check if user wrote something in text and in shift
    text_is_here = False
    shift_is_here = False
    text = input("Type your message:\n").lower()
    # If nothing in text, we change our flag
    if text == '':
        print('You need to paste anything!')
        time.sleep(1.5)
        continue
    else:
        text_is_here = True
    # If something wrong with shift, we change our flag
    # noinspection PyBroadException
    try:
        shift = int(input("Type the shift number:\n"))
        shift_is_here = True
    except Exception:
        print('You need to type integer value!')
        time.sleep(1.5)
        continue
    # If both flags are True then we start our program
    if text_is_here and shift_is_here:
        caesar(text, shift, direction)

    # Check if user wants to restart program
    restart = input('Type \'yes\' if you want to start again. Otherwise type \'no\'\n')
    if restart == 'yes':
        pass
    elif restart == 'no':
        flag = True

# Less text and easier way
# def caesar(text, shift, direction):
#   just_a_text = ''
#   if shift > 26:
#     shift = shift % 26
#   if direction == 'decode':
#       shift *= -1
#   for letter in text:
#       if letter not in alphabet:
#           just_a_text += letter
#       else:
#         position = alphabet.index(letter)
#         new_position = position + shift
#         just_a_text += alphabet[new_position]
#    print(f"The {direction} text is {just_a_text}")
# flag = False
# while flag == False:
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
# caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
# restart = input('Do you want to restart program?\n')
# if restart == 'yes':
#   pass
# elif restart == 'no':
#   flag = True
