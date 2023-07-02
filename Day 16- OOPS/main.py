from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

flag = True
menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

while flag:
    drink = input("What would you like? " + menu.get_items() + " ")
    menuItem = menu.find_drink(drink)

    if drink == "off":
        flag = False

    elif drink == "report":
        coffeeMaker.report()
        moneyMachine.report()

    else:
        if coffeeMaker.is_resource_sufficient(menuItem) and moneyMachine.make_payment(
            menuItem.cost
        ):
            coffeeMaker.make_coffee(menuItem)
