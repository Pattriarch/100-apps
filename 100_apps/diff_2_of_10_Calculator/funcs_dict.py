def add(first_num, second_num):
    return round(first_num + second_num, 2)

def substract(first_num, second_num):
    return round(first_num - second_num, 2)

def multiply(first_num, second_num):
    return round(first_num * second_num, 2)

def divide(first_num, second_num):
    return round(first_num / second_num, 2)

def square(first_num, second_num):
    return round(first_num ** second_num, 2)


operations = {
    '+':add,
    '-':substract,
    '*':multiply,
    '/':divide,
    '**':square,
}