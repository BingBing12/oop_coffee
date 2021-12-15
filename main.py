from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
maker = CoffeeMaker()
money = MoneyMachine()
is_off = False
while not is_off:
    print(menu.get_items())
    choice = input("Please select your drink: ")
    if choice == "off":
        is_off = True
    elif choice == "report":
        maker.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        if drink is not None and maker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            maker.make_coffee(drink)




