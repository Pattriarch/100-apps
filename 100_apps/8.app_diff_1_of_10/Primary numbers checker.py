primenum = "It's a prime number."
notprimenum = "It's not a prime number."


def prime_checker(number):
  q = True
  if number == 0 or number == 1:
    return print(notprimenum)
  elif number == 2:
    return print(primenum)
  elif number > 1:
    for i in range(2, number - round(number/2)+1):
      if number % i == 0:
        return print(notprimenum)
      else:
        q = False
  if q == False:
    print(primenum)

n = int(input("Check this number: "))
prime_checker(number=n)