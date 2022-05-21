menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


# to check if resources required by coffee are available or not.

def check_res(cafe):
    if menu[cafe]["ingredients"]["water"] > resources["water"]:
        print('Sorry, not enough water.')
        return False
    if cafe != "espresso" and menu[cafe]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry, not enough milk.")
        return False
    if menu[cafe]["ingredients"]["coffee"] > resources["coffee"]:
        print('Sorry, not enough coffee.')
        return False
    return True


#  Updating the resources

def update_res(cafe):
    resources["water"] -= menu[cafe]["ingredients"]["water"]
    if cafe != "espresso":
        resources["milk"] -= menu[cafe]["ingredients"]["milk"]
    resources["coffee"] -= menu[cafe]["ingredients"]["coffee"]


# check if enough money

def process_coins(cafe):
    print('Please insert coins:')
    quarters = float(input('How many quarters?: '))
    nickels = float(input('How many nickels?: '))
    dime = float(input('How many dimes?: '))
    penny = float(input('How many pennies?: '))
    costs = quarters * 0.25 + nickels * 0.05 + dime * 0.10 + penny * 0.01
    if costs < menu[cafe]["cost"]:
        print('Not enough money.')
        return False
    else:
        resources["money"] += menu[cafe]["cost"]
        update_res(cafe)
        # "{:.2f}".format(value)
        c = costs - menu[cafe]["cost"]
        print(f'Here\'s your change: ${"{:.2f}".format(c)}')
        return True


# Print report of how many resource available

def report():
    for key in resources:
        print(f'{key} : {resources[key]}')


ch = True

while ch:
    cafe = input('What would you like? (espresso($1.5)/latte($2.5)/cappuccino($3.0)):').lower()
    if cafe == 'report':
        report()
    elif cafe == 'latte':
        if check_res(cafe):
            if process_coins(cafe):
                print(f"Here is your {cafe}. Enjoy!")
    elif cafe == 'espresso':
        if check_res(cafe):
            if process_coins(cafe):
                print(f"Here is your {cafe}. Enjoy!")
    elif cafe == 'cappuccino':
        if check_res(cafe):
            if process_coins(cafe):
                print(f"Here is your {cafe}. Enjoy!")
    # only the operator can turn off the machine and knows the keyword "off" to do so.
    elif cafe == 'off':
        ch = False
