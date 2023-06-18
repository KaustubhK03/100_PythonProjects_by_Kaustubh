from art import logo
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
}


def report(resources):
    for key in resources:
        print(f"{key} : {resources[key]}")


def check_sufficiency(resources):
    if prompt == "latte" or prompt == "cappuccino":
        if resources["water"] < MENU[prompt]["ingredients"]["water"]:
            print("Sorry but there is not enough water in the coffee machine! \n")
        elif resources["milk"] < MENU[prompt]["ingredients"]["milk"]:
            print("Sorry but there is not enough milk in the coffee machine! \n")
        elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry but there is not enough coffee in the coffee machine! \n")
        else:
            Process_coins()
    else:
        if resources["water"] < MENU[prompt]["ingredients"]["water"]:
            print("Sorry but there is not enough water in the coffee machine! \n")
        elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry but there is not enough coffee in the coffee machine! \n")
        else:
            Process_coins()


def minus_resources(prompt):
    if prompt == "espresso":
        resources["water"] = resources["water"] - MENU[prompt]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU[prompt]["ingredients"]["coffee"]
    else:
        resources["water"] = resources["water"] - MENU[prompt]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU[prompt]["ingredients"]["coffee"]
        resources["milk"] = resources["milk"] - MENU[prompt]["ingredients"]["milk"]


def Process_coins():
    quarters = int(input("Enter no of quarters: "))
    dimes = int(input("Enter no of dimes: "))
    nickles = int(input("Enter no of nickles: "))
    pennies = int(input("Enter no of pennies: "))
    global monetary_value
    monetary_value = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    Transaction_successfull(monetary_value)


def Transaction_successfull(monetary_value):
    if monetary_value == MENU[prompt]["cost"]:
        minus_resources(prompt)
        global profit
        profit = MENU[prompt]["cost"]
        if "profit" in resources:
            resources["profit"] = resources["profit"] + profit
        else:
            resources["profit"] = profit
        print(f"Here is your ${prompt} ☕️, Enjoy!\n")
    elif monetary_value > MENU[prompt]["cost"]:
        minus_resources(prompt)
        profit = MENU[prompt]["cost"]
        if "profit" in resources:
            resources["profit"] = resources["profit"] + profit
        else:
            resources["profit"] = profit
        change = monetary_value - MENU[prompt]["cost"]
        change = round(change, 2)
        print(f"Here is ${change} change.")
        print(f"Here is you {prompt}, Enjoy!\n")
    else:
        print("Sorry that's not enough money. Money refunded.\n")


def make_coffee():
    check_sufficiency(resources)


def refill():
    while resources["water"] <= 300:
        resources["water"] = resources["water"] + 50
    while resources["milk"] <= 200:
        resources["milk"] = resources["milk"] + 100
    while resources["coffee"] <= 100:
        resources["coffee"] = resources["coffee"] + 18
    print("Coffee Machine Refilled Successfully!\n")


print(logo)
while True:
    prompt = input("What would you like? (espresso/latte/cappuccino):").lower()
    if prompt == 'off':
        print("Signing Off🫡")
        exit()
    elif prompt == "report":
        report(resources)
    elif prompt == "refill":
        refill()
    else:
        make_coffee()


