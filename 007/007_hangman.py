#gra hangman przed uruchomieniem gry trzeba zainstalować bibbliotekę random-word

from random_word import RandomWords

def main() -> None:
    """The hangman game"""

    hangman_stages: list[str] = [
        """
         -----
         |   |
             |
             |
             |
             |
        --------
        """,
        """
         -----
         |   |
         O   |
             |
             |
             |
        --------
        """,
        """
         -----
         |   |
         O   |
         |   |
             |
             |
        --------
        """,
        """
         -----
         |   |
         O   |
        /|   |
             |
             |
        --------
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
             |
             |
        --------
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        /    |
             |
        --------
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        --------
        """
    ]
    #Generuje randomowe słowo
    r: RandomWords = RandomWords()
    random_word:str = r.get_random_word()
    #print(random_word)

    lives_counter:int = 6
    hangman_stages_num:int = 0

    empty_string: str = "_"
    for i in range(len(random_word)):
        empty_string += "_"
    print(empty_string)

    empty_list = list(empty_string)
    print(hangman_stages[hangman_stages_num])
    #tworze stringa a później lsitę z _ o długości wygenerowanego słowa

    while lives_counter > 0:  #licznik żyć
        i = 0  #licznik pozycji litery w słowie





        pl_letter:str = input("Please give me the letter: ")
        if pl_letter in empty_list:
            print(f"That letter {pl_letter} is already in the word ")

        found_letter:bool = False #bool od znalezienia litery



        for letter in random_word:
            if pl_letter == letter:
                print(f"Found {pl_letter} at {i}")
                empty_list[i] = pl_letter
                found_letter = True #litera znaleziona
            i += 1
            #litera znaleziona licznik rpzechodzi dalej na w poszukwianiu litery na innej pozycji

        if not found_letter: #jak nie znalazł litery
            hangman_stages_num += 1
            print(hangman_stages[hangman_stages_num])
            lives_counter -= 1 #życie w dól o 1
            print(f"Wrong guess! Lives left: {lives_counter}")
        else:
            print("Good guess!")

        if "_" not in empty_list:
            print(f"Congratulations you WON! The word was {random_word}")

        if lives_counter == 0:
            print("Game Over you lost! ")

        empty_string = "".join(empty_list)
        print(empty_string)


if __name__ == "__main__":
    main()