from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine, coffee_maker, menu = MoneyMachine(), CoffeeMaker(), Menu()

choice = input(f"What would you like? ({menu.get_items()}): ")
while choice != 'off':
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    else: print("Invalid choice. Try Again")
    choice = input("What would you like? (espresso/latte/cappuccino): ")