import sys



MENU:dict = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    }
}

express_res:dict = { "ingredients": {
            "water": 300,
            "milk": 200,
            "coffee": 100,
            }
                }
money_inside:dict = {
    "money": 3.0
    }


def drink_menu() -> str:
    """Function used for coffee express menu"""
    on:bool = True
    while on:
        coffee:str = input("What would you like: espresso/latte/cappuccino: ").lower().strip()
        if coffee == "espresso":
            print("You chose an espresso ")
            return coffee
        elif coffee == "latte":
            print("You chose latte.")
            return coffee
        elif coffee == "cappuccino":
            print("You chose cappuccino")
            return coffee
        elif coffee == "off":
            print("Coffee machine is turning off")
            print("brrrr Flushing..beep")
            print("Coffee machine is of. ")
            sys.exit()
        elif coffee == "report":
            print("checking the ingredients")
            express_resources()
        else:
            print("You can only choose from espresso/latte/cappuccino")


def express_resources() -> None:
    """Function created to check  the level of water,coffee and milk in express"""
    print(f"Total level of milk: {express_res['ingredients']['milk']} ml.")
    print(f"Total level of water: {express_res['ingredients']['water']} ml.")
    print(f"Total level of coffee: {express_res['ingredients']['coffee']} g.")
    print(f"""Total amount of money: {money_inside['money']} $""")
    total_milk:int = express_res['ingredients']['milk']
    total_water:int = express_res['ingredients']['water']
    total_coffee:int = express_res['ingredients']['coffee']


def coin_inlet(coffee:str) ->bool:
    """Function counts the coins"""
    drink_cost: float = MENU[coffee]["cost"]
    coin:list[float] = []
    coin_add: bool = True
    user_sum:float = 0

    while coin_add:
        coin = input(f"""The cost of the drink is{MENU[coffee]["cost"]}input coins quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01: """ )
        if coin == "quarter":
            user_sum += 0.25
            print(user_sum)
        elif coin == "dime":
            user_sum += 0.10
            print(user_sum)
        elif coin == "nickel":
            user_sum += 0.05
            print(user_sum)
        elif coin == "penny":
            user_sum += 0.01
            print(user_sum)
        elif coin == "stop":
            coin_add = False
            print(f"You got:{user_sum} $")
            print("checking the money...")
            if user_sum >= drink_cost:
                print("preparing the drink")
                change: float = user_sum - drink_cost
                if change > 0:
                    print("""blink...here's your change""")


                    return True
            elif user_sum < drink_cost:
                print("Sorry not enough money")
                return False


def resources_check(coffee:str) -> bool:
    """Function check the coffee,milk and water levels"""

    selected_coffee_ingredients = MENU[coffee]
    print(selected_coffee_ingredients)

    needed_water:int = MENU[coffee]["ingredients"]['water']
    needed_coffee:int = MENU[coffee]["ingredients"]['coffee']
    needed_milk = selected_coffee_ingredients.get('milk', 0) #czasem mlekonie jest potrzebnye i wtedy )
    total_milk: int = express_res['ingredients']['milk']
    total_water: int = express_res['ingredients']['water']
    total_coffee: int = express_res['ingredients']['coffee']

    # if total_milk > needed_milk and total_coffee > needed_coffee and total_water > needed_water:
    #     return True
    # elif total_coffee > needed_coffee and total_water > needed_water:
    #     return True
    # else:
    #     return False

    if total_water < needed_water:
        return False
    if total_coffee < needed_coffee:
        return False
    if total_milk < needed_milk:
        return False
    return True


def make_coffee(coffee:str) -> bool:
    """Function responsible for making the coffee"""
    print(f"Bzzzztt {coffee} is ready.")

    coffee_left: int = 0
    milk_left: int = 0
    water_left: int = 0
    express_res['ingredients']['coffee'] -= MENU[coffee]["ingredients"]['coffee']
    express_res['ingredients']['milk'] -= MENU[coffee]["ingredients"].get('milk', 0)
    express_res['ingredients']['water'] -= MENU[coffee]["ingredients"]['water']


def main() -> None:
    while True:
        coffee = drink_menu()
        if resources_check(coffee) == True and coin_inlet(coffee) == True:
            make_coffee(coffee)
        else:
            print("No coffee this time!")


if __name__ == "__main__":
    main()
