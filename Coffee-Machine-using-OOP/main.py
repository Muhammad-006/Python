from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


item = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()
while True:
    item = Menu()
    choice = input(f"What do you want? ({item.get_items()}): ")
    if choice == 'off':
        break
    elif choice == 'report':
        coffee.report()
        money.report()
    else:
        item = (item.find_drink(choice))
        if coffee.is_resource_sufficient(item):
            if money.make_payment(item.cost):
                coffee.make_coffee(item)
        else:
            print("Sorry we don't have enough stock for this product")


