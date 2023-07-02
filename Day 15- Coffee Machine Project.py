MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    },
}

resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}


def checkResources(choice, amt, flag1):
    for k in resources:
        if k != "money":
            if not (resources[k] - MENU[choice]["ingredients"][k]) > 0 and k == "water":
                flag1 = 0
                print("There's not enough " + k)
                return flag1
            elif (
                not (resources[k] - MENU[choice]["ingredients"][k]) > 0 and k == "milk"
            ):
                flag1 = 0
                print("There's not enough " + k)
                return flag1
        elif not amt - MENU[choice]["cost"] > 0 and k == "money":
            flag1 = 0
            print("There's not enough " + k)
            return flag1
        else:
            flag1 = 1

    return flag1


def updateResources(choice, amt):
    for k in resources:
        if k != "money":
            resources[k] = resources[k] - MENU[choice]["ingredients"][k]
        elif (amt - MENU[choice]["cost"]) > 0 and k == "money":
            change = round((amt - MENU[choice]["cost"]), 2)
            print(f"Your change is {change}")
            resources[k] = resources[k] + MENU[choice]["cost"]


def updateValues(choice):
    if choice == "off":
        flag = False
        return flag
    elif choice == "report":
        for key in resources:
            if key == "water" or key == "milk":
                print(key + " : " + str(resources[key]) + "ml")
            elif key == "coffee":
                print(key + " : " + str(resources[key]) + "gm")
            else:
                print(key + " : $" + str(resources[key]))
    else:

        print("Please insert coins.")
        q = float(input("How many quarters?: "))
        q = q * 0.25
        d = float(input("How many dimes?: "))
        d = d * 0.10
        n = float(input("How many nickles?: "))
        n = n * 0.05
        p = float(input("How many pennies?: "))
        p = p * 0.01
        total = q + d + n + p
        flag1 = 0
        flag1 = checkResources(choice, total, flag1)
        if flag1 == 1:
            updateResources(choice, total)
            print("Your order for " + choice + " is Ready !!")
    flag = True
    return flag


flag = True
while flag:

    choice = input("What would you like? (espresso/latte/cappuccino): ")

    flag = updateValues(choice)
