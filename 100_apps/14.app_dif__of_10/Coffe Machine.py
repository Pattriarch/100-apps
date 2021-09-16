from Menu_profit_and_resources import MENU
from Menu_profit_and_resources import resources

profit = 0


def check_resources(user_decide):
    if resources["water"] > MENU[user_decide]["ingredients"]["water"]:
        pass
    else:
        return print("Sorry, there's not enough water.")
    if "milk" in MENU[user_decide]["ingredients"]:
        if resources["milk"] >= MENU[user_decide]["ingredients"]["milk"]:
            pass
        else:
            return print("Sorry, there's not enough milk.")
    else:
        pass
    if resources["coffee"] >= MENU[user_decide]["ingredients"]["coffee"]:
        pass
    else:
        return print("Sorry, there's not enough coffee.")
    return True


def spend_resources(user_decide):
    if "milk" in MENU[user_decide]["ingredients"]:
        resources["milk"] -= MENU[user_decide]["ingredients"]["milk"]
    resources["water"] -= MENU[user_decide]["ingredients"]["water"]
    resources["coffee"] -= MENU[user_decide]["ingredients"]["coffee"]


def coins(user_decide):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    user_money = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if user_money >= MENU[user_decide]["cost"]:
        change = user_money - MENU[user_decide]["cost"]
        global profit
        profit += MENU[user_decide]["cost"]
        if user_money > MENU[user_decide]["cost"]:
            print(f"Here is ${round(change, 2)} in change.")
        else:
            print('No change.')
        pass
    else:
        print("Sorry that's not enough money. Money refunded.")
        return True


turn_on = True
while turn_on:
    decide = input("What would you like? (espresso/latte/cappuccino): ")

    if decide.lower() == "report":
        print(f'Water: {resources["water"]}ml\n'
              f'Milk: {resources["milk"]}ml\n'
              f'Coffee: {resources["coffee"]}g\n'
              f'Money: ${profit}')
    elif decide.lower() == "off":
        print('Your coffee machine now is off')
        global turn_off
        turn_on = False
    else:
        status_resources = check_resources(decide)
        if status_resources:
            status_coins = coins(decide)
            if not status_coins:
                spend_resources(decide)
                print(f"Here is your {decide} ☕. Enjoy! ")
