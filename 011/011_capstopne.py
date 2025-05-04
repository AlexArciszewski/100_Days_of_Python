import random
# def program_logo():
#     logo = """
#     .------.            _     _            _    _            _
#     |A_  _ |.          | |   | |          | |  (_)          | |
#     |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
#     | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
#     |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
#     `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
#           |  \/ K|                            _/ |
#           `------'                           |__/
#     """
#     print(logo)

def welcome_menu():
    play_or_quit = input("To play the game pres: p. To quit press: q ")
    if play_or_quit == "p":
        print("Loading the game...")
    elif play_or_quit == "q":
        print("The program will now exit")
    else:
        print("Wrong button")

def card_deck():
    colors = ["Spades", "Clubs", "Diamonds", "Hearts"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    point_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}

    deck = [(color, value, point_values[value]) for color in colors for value in values]

    # print(deck)
    return deck


def player_choose_your_card(deck):
    # deck = card_deck()
    chosen_card_player = random.choice(deck)
    print(f"Chosen card by a Player is: {chosen_card_player} You got {chosen_card_player[2]} points")

    # points.append(chosen_card_player[2])
    # print(f"you have now {chosen_card_player[2]}")
    return chosen_card_player

def computer_choose_your_card_no_1(deck):
    # deck = card_deck()
    first_chosen_card_computer = random.choice(deck)
    # print(f"Chosen card is: {chosen_card_computer} You got {chosen_card_computer[2]} points")
    # points = points_player()
    # points.append(chosen_card_computer[2])
    # print(f"you have now {chosen_card_computer[2]}")
    print("the card chosen by computer is hidden at the moment")
    return first_chosen_card_computer

def computer_choose_your_card_no_2_3(deck):
    # deck = card_deck()
    second_third_chosen_card_computer = random.choice(deck)
    print(f"Next card chosen by computer is: {second_third_chosen_card_computer} Computer has {second_third_chosen_card_computer[2]} points")
    # points = points_player()
    # points.append(chosen_card_computer[2])
    # print(f"you have now {chosen_card_computer[2]}")
    return second_third_chosen_card_computer

def question_taking_another_card():
    print("At the moment the")


def score_board():
    scores = adding_points_to_a_score_boards()
    score_board_computer = []
    score_board_player = []
    x = scores[0]
    y = scores[1]
    score_board_player.append(x)
    score_board_computer.append(y)
    if x > y:
        message = print(f"player leads with{x} points")
    else:
        message = print(f"Computer leads with{y} points")
    return message

def adding_points_to_a_score_boards():
    deck = card_deck()
    card1 = player_choose_your_card(deck)
    card2 = computer_choose_your_card_no_2_3(deck)
    card3 = computer_choose_your_card_no_2_3(deck)


    player_points = card1[2]
    computer_points_1 = card2[2]
    computer_points_2 = card3[2]
    computer_points_1st_round = computer_points_1 + computer_points_2
    added_points = [player_points, computer_points_1st_round]
    return added_points








# def adding_cards_player([score_board_player, score_board_computer]):
#     score_board_player.append(chosen_card_player[2])
#     score_board_computer.append(chosen_card_computer[2])





def main():
    # program_logo()
    welcome_menu()
    card_deck()
    deck = card_deck()
    player_choose_your_card(deck)
    computer_choose_your_card_no_1(deck)
    computer_choose_your_card_no_2_3(deck)

    adding_points_to_a_score_boards()
    score_board()
    # card1 = player_choose_your_card()
    # card2 = computer_choose_your_card_no_2_3()
    # card3 = computer_choose_your_card_no_2_3()
    # adding_points_to_a_score_boards()
    # chosen_card_player = player_choose_your_card(deck)
    # first_chosen_card_computer = computer_choose_your_card_no_1(deck)
    # second_chosen_card_computer = computer_choose_your_card_no_2_3(deck)
    # third_chosen_card_computer = computer_choose_your_card_no_2_3(deck)


if __name__ == "__main__":
    main()