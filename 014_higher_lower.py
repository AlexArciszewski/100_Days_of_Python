from data_for_high_low_game import data
from typing import Callable, Dict
import random
import sys

def show_intro() -> None:
    """Function used to show the game logo"""

    logo:str = """    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/__      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/   """


    print(logo)



def data_import() -> None:
    """Function used for data import"""

    data_import.comp_data:list[dict] = data


def item_to_compare() ->None:
    """game logic"""
    data_import.comp_data:list[dict] = data
    random.shuffle(data)

    lifes: int = 1
    points: int = 0

    while lifes > 0:

        if len(data) < 2:
            print("Congrats you finished the game.")
            break

        a_choice: dict = data.pop()
        print(a_choice["name"])

        logo_b: str = """
_    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)"""
        print(logo_b)

        b_choice: dict = data.pop()
        print(b_choice["name"])

        top_followers:str = ""

        user_choice:str = input("""Who has more followers 'A' or 'B': """)
        if user_choice == 'A':
            if a_choice["follower_count"] > b_choice["follower_count"]:
                top_followers == a_choice
                points += 1
                print(f"Current score:{points}")
            elif a_choice["follower_count"] < b_choice["follower_count"]:
                lifes = 0
                print("Game Over")
                print(f"Current score:{points}")
        elif user_choice == 'B':
            if b_choice["follower_count"] > a_choice["follower_count"]:
                top_followers == b_choice
                points +=1
                print(f"Current score:{points}")
            elif b_choice["follower_count"] < a_choice["follower_count"]:
                lifes = 0
                print(f"Current score:{points}")
                print("Game Over")


def exit_game() -> None:
    """Function for game exit"""
    sys.exit()


def menu() -> None:
    """Function to show the menu"""
    print("Welcome to the Higher Lower Game!\n")
    print("To play the game press 1. press 2 for exit")
    print("1 - Start the game")
    print("2 - Exit")


def main() -> None:
    show_intro()
    options: Dict[int, Callable[[], None]] ={
        1: lambda:(show_intro(), data_import(), item_to_compare()),
        2: exit_game,

    }

    while True:
        menu()
        try:
            user_choice:int = int(input("Choose your option: "))
        except ValueError:
            print("You have tu press the number to continue.")
            continue
        if user_choice in options:
            options[user_choice]()
        else:
            print("Incorrect button.")


if __name__ == "__main__":
    main()
