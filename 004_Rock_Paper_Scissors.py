import random

def main() -> None:
    """metod usd for creating the program"""
    players_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: "))

    ascii_art = {
        0: """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """,
        1: """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """,
        2: """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """
    }
    option_list = list(ascii_art.keys())
    computer_choice = random.choice(list(ascii_art.keys()))
    print(ascii_art[computer_choice])


    if players_choice in ascii_art.keys():
        print(ascii_art[players_choice])

        if computer_choice  == players_choice:
            print("Draw")
        elif computer_choice == 2 and players_choice == 0:
            print(f"player wins")
        elif computer_choice== 1 and players_choice == 2:
            print("player wins")
        elif computer_choice == 0 and players_choice == 1:
            print("player wins")
        else:
            print("computer wins")


if __name__ == "__main__":
    main()