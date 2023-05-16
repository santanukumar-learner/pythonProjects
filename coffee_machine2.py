MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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


def is_ingedients_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print("sorry there is no sufficient ingredients. ")
            return False
    return True


def processing_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_recieved, drink_cost):
    if money_recieved >= drink_cost:
        global profit
        profit += drink_cost
        change = round(money_recieved - drink_cost, 2)
        print(f"here is your {change}$ change")
        return True
    else:
        print(f"money is not sufficient here is your {money_recieved}")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your drink {drink} ")


profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
is_on = True
while is_on:
    type = input("what type of coffee do you want: ").lower()
    if type == "off":
        is_on = False
    elif type == "report":
        print(f"water = {resources['water']}, milk = {resources['milk']} coffee = {resources['coffee']}")
        print(f"income = {profit}$")

    else:
        drink = MENU[type]
        if is_ingedients_sufficient(drink["ingredients"]):
            payment = processing_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(type, drink["ingredients"])

