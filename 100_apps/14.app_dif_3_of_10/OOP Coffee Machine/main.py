from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# Drinks
espresso = MenuItem("espresso", 50, 0, 18, 1.5)
latte = MenuItem("latte", 200, 150, 24, 2.5)
cappuccino = MenuItem("cappuccino", 250, 100, 24, 3.0)

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    options = menu.get_items()
    order_name = input(f'What would you like? ({options}): ')
    if order_name == 'report':
        coffee_maker.report()
        money_machine.report()
    elif order_name == 'off':
        is_on = False
    else:
        drink = menu.find_drink(order_name)
        is_enough_res = coffee_maker.is_resource_sufficient(drink)
        if is_enough_res:
            is_enough_mon = money_machine.make_payment(drink.cost)
            money_machine.money_received = 0
            if is_enough_mon:
                coffee_maker.make_coffee(drink)

