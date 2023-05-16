from CF import MENU
make_again = True


while make_again:
    flavour = input("what type of coffee do you want 'latte', 'cappuccino' or 'espresso'").lower()
    report = {
        "milk_report": 400,
        "water_report": 500,
        "coffee_report": 100
    }
    milk_report = report["milk_report"]
    water_report = report["water_report"]
    coffee_report = report["coffee_report"]
    if flavour == "cappuccino":
        milk = MENU["cappuccino"]["ingredients"]["milk"]
        water = MENU["cappuccino"]["ingredients"]["water"]
        coffee = MENU["cappuccino"]["ingredients"]["coffee"]
        money = MENU["cappuccino"]["cost"]

    elif flavour == "latte":
        milk = MENU["latte"]["ingredients"]["milk"]
        water = MENU["latte"]["ingredients"]["water"]
        coffee = MENU["latte"]["ingredients"]["coffee"]
        money = MENU["latte"]["cost"]
    if milk_report > milk and water_report > water and coffee_report > coffee:
        print(f"give {money} rupees")
        money_given = int(input(f"give {money}Rs"))
        if money_given > money:
            change = money_given - money
            print(f"Thank you here is your {flavour} and your {change}Rs")
            milk_report -= milk
            coffee_report -= coffee
            water_report -= water
        elif money == money_given:
            print(f"Thank you here is your {flavour}")
        money_report += money_given
    else:
        print("There is no sufficient ingredient")

    money_report = 0
    if flavour == "report":
        print(f"milk = {milk_report}, water = {water_report}, coffe = {coffee_report}")
    elif flavour == "off":
        make_again = False

    elif flavour == "espresso":
        water = MENU["espresso"]["ingredients"]["water"]
        coffee = MENU["espresso"]["ingredients"]["coffee"]
        money = MENU["espresso"]["cost"]

        if water_report > water and coffee_report > coffee:
            print(f"give {money} rupees")
            money_given = int(input(f"give {money}Rs"))
            if money_given > money:
                change = money_given - money
                print(f"Thank you here is your {flavour} and your {change}Rs")
                milk_report -= milk
                coffee_report -= coffee
                water_report -= water
            elif money == money_given:
                print(f"Thank you here is your {flavour}")
            money_report += money_given
        else:
            print("There is no sufficient ingredient")