import random

def main() -> None:
    """Rock, Paper, Scissors game"""
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

    try:
        players_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: "))
        if players_choice not in ascii_art:
            print("Invalid number. Please choose 0, 1 or 2.")
            return
    except ValueError:
        print("Invalid input. Please enter a number (0, 1 or 2).")
        return

    computer_choice = random.choice(list(ascii_art.keys()))

    print("\nYou chose:")
    print(ascii_art[players_choice])
    print("Computer chose:")
    print(ascii_art[computer_choice])

    if computer_choice == players_choice:
        print("Result: Draw")
    elif computer_choice == 2 and players_choice == 0:
        print("Result: Player wins")
    elif computer_choice == 1 and players_choice == 2:
        print("Result: Player wins")
    elif computer_choice == 0 and players_choice == 1:
        print("Result: Player wins")
    else:
        print("Result: Computer wins")

if __name__ == "__main__":
    main()