import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to the PyPassword Generator!')
letter = int(input('How many letters would you like in your password?\n'))
number = int(input('How many numbers would you like?\n'))
symbol = int(input('How many symbols would you like?\n'))

password = ''

# Easy level
for i in range(letter):
    password += random.choice(letters)
for i in range(number):
    password += random.choice(numbers)
for i in range(symbol):
    password += random.choice(symbols)

print('Easy variation:', password)

passwd = ''

# Middle level
password_list = []

for i in range(letter):
    password_list += random.choice(letters)

for i in range(number):
    password_list += random.choice(numbers)

for i in range(symbol):
    password_list += random.choice(symbols)

random.shuffle(password_list)

pas = ''
for i in password_list:
    pas += i

print('Middle variation:', pas)

# Hard level
while (letter > 0) or (symbol > 0) or (number > 0):
    flag = random.randint(1, 3)
    if flag == 1 and letter > 0:
        passwd += random.choice(letters)
        letter -= 1
    else:
        pass
    if flag == 2 and number > 0:
        passwd += random.choice(numbers)
        number -= 1
    else:
        pass
    if flag == 3 and symbol > 0:
        passwd += random.choice(symbols)
        symbol -= 1
    else:
        pass

print('Hard variation:', passwd)