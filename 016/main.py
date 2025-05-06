from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



# coffeeexpress = CoffeeMaker()
# coffeeexpress.report()
#
# my_coffee = MenuItem("espresso", water=50, milk=0, coffee=18, cost=1.5)
# print(coffeeexpress.is_resource_sufficient(my_coffee))
# profit = MoneyMachine()
# print(profit.make_payment(my_coffee))
# print(profit.report(my_coffee))
# print(profit.process_coins(my_coffee))

money_machine = MoneyMachine()
coffeemaker = CoffeeMaker()
menu = Menu()
is_on = True
my_coffee = MenuItem("espresso", water=50, milk=0, coffee=18, cost=1.5)
money_machine.report()
coffeemaker.report()
print(coffeemaker.is_resource_sufficient(my_coffee))

while is_on:
    options = menu.get_items()
    choice =input(f"What you want {options} ? ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffeemaker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffeemaker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffeemaker.make_coffee(drink)




