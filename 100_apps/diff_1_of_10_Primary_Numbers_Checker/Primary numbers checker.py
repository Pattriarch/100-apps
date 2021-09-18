prime_num = "It's a prime number."
not_prime_num = "It's not a prime number."


def prime_checker(number):
    q = True
    if number == 0 or number == 1:
        return print(not_prime_num)
    elif number == 2:
        return print(prime_num)
    elif number > 1:
        for i in range(2, number - round(number / 2) + 1):
            if number % i == 0:
                return print(not_prime_num)
            else:
                q = False
    if not q:
        print(prime_num)


n = int(input("Check this number: "))
prime_checker(number=n)
