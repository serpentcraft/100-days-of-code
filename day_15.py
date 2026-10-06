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

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}

money = 0

def resources_checking():
    '''Reporting how much resources the machine has.'''
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

def resource_sufficiency(drink_name):
    '''Checks the sufficiency of the resources and returns True or False.'''
    ingredients = MENU[drink_name]["ingredients"]
    missing = []
    for ingredient, needed in ingredients.items():
        if resources[ingredient] < needed:
            missing.append(ingredient)

    if missing:
        print(f"Sorry, not enough: {', '.join(missing)}")
        return False
    return True

def process_coins():
    '''Asks how many coins user inserted and counts the total amount.'''
    total = 0
    for coin_name, coin_value in coins.items():
        while True:
            try:
                count = int(input(f"How many {coin_name}? "))
                break
            except ValueError:
                print("Please enter a number.")
        total += coin_value * count
    return total

def transaction(total_inserted, final_cost, drink_name):
    '''Checks if the transaction is successful and returns True or False.'''
    if total_inserted >= final_cost:
        change = total_inserted - final_cost
        if change > 0:
            print(f"Here's your change: ${change:.2f}.")
        return True
    else:
        print(f"Sorry, not enough money for {drink_name}. Money refunded.")
        return False

def resources_deduction(drink_name):
    '''Deducts needed ingredients from resources and changes values in resources dictionary.'''
    ingredients = MENU[drink_name]["ingredients"]
    for ingredient, needed in ingredients.items():
        resources[ingredient] -= needed

coffee_making = True

while coffee_making:
    drink_name = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if drink_name == "off":
        coffee_making = False
        print("Coffee machine is turned off.")
        continue

    if drink_name == "report":
        resources_checking()
        continue

    if drink_name not in ["espresso", "latte", "cappuccino"]:
        print("Sorry, that's not a valid option.")
        continue

    if resource_sufficiency(drink_name):
        final_cost = MENU[drink_name]["cost"]
        print(f"One {drink_name} costs: ${final_cost}. Please insert coins: ")
        total_inserted = process_coins()
        print(f"You inserted: ${total_inserted:.2f}")

        if transaction(total_inserted, final_cost, drink_name):
            money += final_cost
            resources_deduction(drink_name)
            print(f"Here's your {drink_name}. Enjoy the drink! ☕")
