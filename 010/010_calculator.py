from typing import Callable, Dict

def show_logo() -> None:

    logo = """                888                888        888                   
                888                888        888                   
                888                888        888                   
 .d8888b 8888b. 888 .d8888b888  888888 8888b. 888888 .d88b. 888d888 
d88P"       "88b888d88P"   888  888888    "88b888   d88""88b888P"   
888     .d888888888888     888  888888.d888888888   888  888888     
Y88b.   888  888888Y88b.   Y88b 888888888  888Y88b. Y88..88P888     
 "Y8888P"Y888888888 "Y8888P "Y88888888"Y888888 "Y888 "Y88P" 888 """
    print(logo)


def menu() -> None:
    print("Menu")


def add() -> None:
    a = float(input("Give me the first number: "))
    b = float(input("Give me the second number: "))
    print(f"The score is: {a + b}")


def substract() -> None:
    a = float(input("Give me the first number: "))
    b = float(input("Give me the second number: "))
    print(f"The score is: {a - b}")


def multiply() -> None:
    a = float(input("Give me the first number: "))
    b = float(input("Give me the second number: "))
    print(f"The score is: {a * b}")


def divide() -> None:
    a = float(input("Give me the first number: "))
    b = float(input("Give me the second number: "))
    print(f"The score is: {a / b}")


def Exit() -> None:
    print("program will now Exit. Have a nice day")


def main() -> None:

    show_logo()


    options: Dict[int, Callable[[], None]] = {
        1: menu,
        2: add,
        3: substract,
        4: multiply,
        5: divide,
        6: Exit,
    }

    while True:
        print("\nChoose options:")
        print("1 - Menu")
        print("2 - Add the numbers")
        print("3 - Substract the numbers")
        print("4 - Multiply the numbers")
        print("5 - Divide the numbers")
        print("6 - Exit")

        try:
            user_choice = int(input("What you want to do? "))
        except ValueError:
            print("Give me the number from the menu")
            continue
        if user_choice in options:
            options[user_choice]()
        else:
            print("wrong choice")


if __name__ == "__main__":
    main()



