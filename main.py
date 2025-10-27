from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_is_on = True

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while machine_is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")

    if choice == "off":
        print("The machine is turned off.")
        machine_is_on = False
    elif choice == "report":
        coffee_maker.report()
    elif choice == "profit":
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink:
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)