from typing import Dict, Callable
import json
import random

def show_logo() -> None:
    logo = """
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
          |  \/ K|                            _/ |                
          `------'                           |__/           
    """
    print(logo)

def show_menu() -> None:
    pass

def deck_creator() -> None:
    cards_types: list[str] = []
    card_figs: list[str] = ["A", "J", "Q", "K"]

    cards: list[str] = [str(card) for card in range(2, 11)]

    cards_types: list = cards + card_figs

    card_colors: list[str] = ["Hearts", "Diamonds", "Clubs", "Spades"]
    card_points: list[int] = [point for point in range(2, 11)]
    #
    card_points.append(11)
    for _ in range(3):
        card_points.append(10)


    card_deck: list = []

    for i in range(len(cards_types)):
        card_type = cards_types[i]
        points = card_points[i]

        for color in card_colors:
            deck_card = {
                'card': card_type,
                'color': color,
                'points': points
            }

            card_deck.append(deck_card)
    deck_creator.card_deck = card_deck




def start_game() -> None:
    """Function used to start the app"""
    starting_cards: list[dict] = []

    random.shuffle(deck_creator.card_deck)

    for i in range(2):
        starting_cards.append(deck_creator.card_deck.pop())

    print(starting_cards)

    cpu_cards: list[dict] = []

    for i in range(2):
        cpu_cards.append(deck_creator.card_deck.pop())

    print(cpu_cards[0])
    print(f"CPU has {cpu_cards[0]['points']} points and one more hidden card")

    for card in starting_cards:
        if card['points'] == 11:
            print("You have the AS")
            value = int(input("pls choose points you want for the AS 1 or 11: "))
            if value == 11:
                print("You chose 11 points")
                card['points'] = 11
            elif value == 1:
                print("you chose 1 point")
                card['points'] = 1
            else:
                print("wrong choice")
                continue

    sum_points: int = starting_cards[0]['points'] + starting_cards[1]['points']
    print(f"Your total points are: {sum_points}")

    if sum_points < 21:
        decide = input("Do you you want one more card? [y/n] ")

        if decide == "y":
            starting_cards.append(deck_creator.card_deck.pop())
            print(starting_cards)

            for card in starting_cards:
                if card['points'] == 11:
                    print("You have the AS")
                    value = int(input("pls choose points you want for the AS 1 or 11"))
                    if value == 11:
                        print("You chose 11 points")
                        card['points'] = 11
                    elif value == 1:
                        print("you chose 1 point")
                        card['points'] = 1
                    else:
                        print("wrong choice")

            sum_points += starting_cards[-1]['points']
            print(f"Your points are {sum_points}")

            if sum_points > 21:
                print("You lost")
                print("Loading main menu....")

            elif sum_points < 21:
                sum_cpu_points = cpu_cards[0]['points'] + cpu_cards[1]['points']

                while sum_cpu_points < 17:
                    new_card = deck_creator.card_deck.pop()
                    cpu_cards.append(new_card)
                    sum_cpu_points += new_card['points']

                    for card in cpu_cards:
                        if card['card'] == 'A' and card['points'] == 11 and sum_cpu_points > 21:
                            card['points'] = 1
                            sum_cpu_points -= 10

                cpu_cards.append(deck_creator.card_deck.pop())
                sum_cpu_points += cpu_cards[1]['points']
                print(f"Total CPU points are {sum_cpu_points}")

                if sum_points > sum_cpu_points and sum_points <= 21:
                    print("You won")
                elif sum_cpu_points > 21:
                    print("You won")
                elif sum_points > sum_cpu_points and sum_points < 21:
                    print("You won")
                else:
                    print("You lost")
                    print("Loading main menu....")

            elif sum_points == 21:
                print("You won")

        elif decide == "n":
            sum_cpu_points = cpu_cards[0]['points'] + cpu_cards[1]['points']
            print(f"Computer points are {sum_cpu_points}")
            print(f"you have total : {sum_points} points")

            if sum_cpu_points <= 21 and sum_cpu_points > sum_points:
                print("You lost.CPU won")
            elif sum_points > 21:
                print("You lost CPU won")
            elif sum_points == sum_cpu_points:
                print("It's a Draw.")
            elif sum_points <= 21 and sum_points > sum_cpu_points:
                print("You won")

    elif sum_points == 21:
        print("You won")














def save_game() -> None:
    pass


def load_game() -> None:
    pass


def exit_game() -> None:
    exit()


def about_game() -> None:
    pass


def main() -> None:
    show_logo()
    deck_creator()

    options: Dict[int, Callable[[], None]] = {
        1: show_menu,
        2: start_game,
        3: save_game,
        4: load_game,
        5: exit_game,
        6:about_game
    }

    while True:
        print("Choose options\n")
        print("1 - Nenu")
        print("2 - New Game")
        print("3 - Save Game")
        print("4 - Load Game")
        print("5 - EXIT")
        print("6 - Help")

        try:
            user_choice:int = int(input("Choose your option: "))
        except ValueError:
            print("You have to give me the number..")
            continue
        if user_choice in options:
            options[user_choice]()
        else:
            print("incorrect number")





if __name__ == "__main__":
    main()