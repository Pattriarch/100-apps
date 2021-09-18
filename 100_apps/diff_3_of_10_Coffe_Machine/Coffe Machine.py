from Menu_profit_and_resources import MENU
from Menu_profit_and_resources import resources

profit = 0


def check_resources(user_decide):
    for item in user_decide:
        if resources[item] < user_decide[item]:
            print(f"Sorry, there's not enough {item}.")
            return False
    return True


def spend_resources(user_decide):
    if "milk" in MENU[user_decide]["ingredients"]:
        resources["milk"] -= MENU[user_decide]["ingredients"]["milk"]
    resources["water"] -= MENU[user_decide]["ingredients"]["water"]
    resources["coffee"] -= MENU[user_decide]["ingredients"]["coffee"]


def coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01


def successful_payment(money, user_drink):
    if money >= user_drink:
        change = money - user_drink
        global profit
        profit += user_drink
        if money > user_drink:
            print(f"Here is ${round(change, 2)} in change.")
        else:
            print('No change.')
        pass
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


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
        drink = MENU[decide]
        drink_price = MENU[decide]["cost"]
        status_resources = check_resources(drink["ingredients"])
        if status_resources:
            user_paid = coins()
            status_pay = successful_payment(user_paid, drink_price)
            if status_pay:
                spend_resources(decide)
                print(f"Here is your {decide} ☕. Enjoy! ")
