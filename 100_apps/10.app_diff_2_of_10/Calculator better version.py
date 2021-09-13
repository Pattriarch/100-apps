from art import logo
from funcs_dict import add
from funcs_dict import substract
from funcs_dict import multiply
from funcs_dict import divide
from funcs_dict import operations

def calculator():
    print(logo)
    cont_prog = True

    first_number = float(input("What's the first number?: "))
    for i in operations:
        print(i)

    while cont_prog == True:
        operation_symbol = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))
        function = operations[operation_symbol]
        answer = function(first_number, second_number)

        print(f'{first_number} {operation_symbol} {second_number} =', answer)

        flag = input(f"Type 'y' to continue calculating with {answer}, or "
              f"type 'n' to start a new calculation: ")
        if flag == 'y':
            first_number = answer
            continue
        elif flag == 'n':
            cont_prog = False
            calculator()

calculator()
