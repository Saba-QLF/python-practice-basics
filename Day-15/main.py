import sys

MENU = {
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


def check_resources(clients_order):
    for ingredient in MENU[clients_order]["ingredients"]:
        if (resources[ingredient] - MENU[clients_order]["ingredients"][ingredient]) < 0:
            print(f"Sorry! Machine does not have enough {ingredient}.")
            return False
    return True

while True:
    clients_order = input("What would you like? (espresso/latte/cappuccino): ")
    if clients_order == "off":
        sys.exit("See you later.")
    elif clients_order == "report":
        for resource in resources:
            print(f"{resource} : {resources[resource]}")
    elif MENU.get(clients_order, 0) != 0:
        enough = check_resources(clients_order)
        if enough:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            sum_of_coins = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
            print(f"Here is ${sum_of_coins} in change.")
            if sum_of_coins > MENU[clients_order]["cost"]:
                for ingredient in MENU[clients_order]["ingredients"]:
                    resources[ingredient] =- MENU[clients_order]["ingredients"][ingredient]
                print(f"Here is your {clients_order} ☕ Enjoy!")
                resources["money"] = sum_of_coins - MENU[clients_order]["cost"]