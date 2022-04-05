##coffee machine 

import logging
logging.basicConfig(filename= 'logfun.log', level = logging.DEBUG, format= "%(asctime)s %(message)s")
data = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee":18,
        },
        "cost":2,
    },
    "latte": {
        "ingredients": {
            "water":200,
            "milk": 150,
            "coffee":24,
        },
        "cost":2.5,
    },
    "cappuccino" : {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0
    }
}
profit = 0
# Resources in the Coffee machine
resources = {
    "water":1000,
    "milk":700,
    "coffee": 800,
}
# checking whether resources are sufficient are not
def is_resources_sufficient(inputs):
    for item in inputs:
        if inputs[item]>= resources[item]:
            print(f'Sorry there is not enough { item}')
    return True

def process_coin():
    total = int(input("How many quarters?"))*0.25
    total += int(input("How many dimes"))*0.1
    total += int(input("How many nickles"))*0.05
    total += int(input("How many pennies"))*0.01
    return total
def is_transaction_ok(money_received, drink_cost):
    if money_received>= drink_cost:
        change = round(money_received- drink_cost,2)
        print(f'Here is {change} in change ')
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that is not enough , money refunded")
        return False
def get_coffee(name, ingreidents):
    for item in ingreidents:
        resources[item] -= ingreidents[item]
    print(f'Here is your {name}')

on = True

while on:


    choice = input("What Would you like (espresso/latte/cappuccino):")

    try:
        if choice =='off':
            on = False
        elif choice == 'report':
            print(f'water: {resources["water"]}ml')
            print(f'milk: {resources["milk"]}ml')
            print(f'coffee: {resources["coffee"]}ml')
            print(f'profit: ${profit}')
        else:
            drink = data[choice]
            if is_resources_sufficient(drink['ingredients']):
                pay = process_coin()
            if is_transaction_ok(pay, drink['cost']):
                get_coffee(choice, drink['ingredients'])
        logging.debug('This is a debug message')
        logging.info('This is an info message')
        logging.warning('This is a warning message')
        logging.error('This is an error message')
        logging.critical('This is a critical message')
    except:
        print("Please Choose any one from this espresso/latte/cappuccino")
