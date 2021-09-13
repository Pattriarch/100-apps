from art import logo

def add(first_num, second_num):
    return first_num + second_num

def substract(first_num, second_num):
    return first_num - second_num

def multiply(first_num, second_num):
    return first_num * second_num

def divide(first_num, second_num):
    return first_num / second_num

operations = {
    '+':add,
    '-':divide,
    '*':multiply,
    '/':divide,
}

q = True
e = True

while e == True:
    print(logo)
    first_number = int(input("What's the first number?: "))
    for i in operations:
        print(i)
    q = True
    while q == True:
        operation_symbol = input("Pick an operation: ")
        second_number = int(input("What's the next number?: "))
        function = operations[operation_symbol]
        answer = function(first_number, second_number)

        print(f'{first_number} {operation_symbol} {second_number} =', answer)

        flag = input(f"Type 'y' to continue calculating with {answer}, or "
              f"type 'n' to start a new calculation: ")
        if flag == 'y':
            first_number = answer
            continue
        elif flag == 'n':
            q = False
