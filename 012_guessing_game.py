from typing import Callable, Dict

import random

def show_logo() -> None:
    logo = """
    █████▀███████████████████████████████████████████████████████████████████████████████████████
    █─▄▄▄▄█▄─██─▄█▄─▄▄─█─▄▄▄▄█─▄▄▄▄███─▄─▄─█─█─█▄─▄▄─███▄─▀█▄─▄█▄─██─▄█▄─▀█▀─▄█▄─▄─▀█▄─▄▄─█▄─▄▄▀█
    █─██▄─██─██─███─▄█▀█▄▄▄▄─█▄▄▄▄─█████─███─▄─██─▄█▀████─█▄▀─███─██─███─█▄█─███─▄─▀██─▄█▀██─▄─▄█
    ▀▄▄▄▄▄▀▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▀▀▄▄▄▀▀▄▀▄▀▄▄▄▄▄▀▀▀▄▄▄▀▀▄▄▀▀▄▄▄▄▀▀▄▄▄▀▄▄▄▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀
    """
    print(logo)


def start_game() -> None:
    """Function used for gaming logic"""
    while True:
        try:
            game_lev: str = input(
                "Choose a difficulty. Type 'easy' or 'hard': "
            ).strip().lower()

            if game_lev not in ('easy', 'hard'):
                raise ValueError("invalid input")
            break

        except ValueError as e:
            print(f"{e}. The available options are: easy or hard ")

    print(f"You chose level {game_lev}")

    chances:int = 0

    if game_lev == "easy":
        chances = 10
    elif game_lev == "hard":
        chances = 5

    print(f"You have now {chances} chances to guess the number.")
    print("I'm thinking of a number between 1 and 100.\n")
    random_num:int = random.randint(1,100)

    while chances > 0:

        guess_num = int(input("Make a guess: "))
        if guess_num > random_num:
            print("Too High.")
            chances -= 1
        elif guess_num < random_num:
            print("Too Low.")
            chances -= 1
        elif guess_num == random_num:
            print("Bingo ")
            print(f"You guessed the number still having {chances} chances")
            break
        else:
            print("something went wrong")

    if chances == 0:
        print("Game Over you lost.\n")


def menu() -> None:
    print("Welcome to the Number Guessing Game!\n")
    print("\nChoose an option. To play again press 1. Press 2 for exit:")
    print("1 - Start the game")
    print("2 - Exit")


def exit_game() -> None:
    print("The program will now exit..")
    exit()


def main() -> None:
    show_logo()


    options: Dict[int, Callable[[], None]] = {
        1: start_game,
        2: exit_game,

    }

    while True:
        menu()
        try:
            user_choice = int(input("Choose your option: "))
        except ValueError:
            print("You have to give me the number listed above.")
            continue
        if user_choice in options:
            options[user_choice]()
        else:
            print("incorrect number please try again. ")


if __name__ == "__main__":
    main()


