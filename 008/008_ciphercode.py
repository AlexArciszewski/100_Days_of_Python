from typing import Callable, Dict
import string
import json


def print_logo() -> None:
    """Function used to print the program logo"""
    logo = """           
     ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
    a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
    8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
    "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
     `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
                88             88                                 
               ""             88                                 
                              88                                 
     ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
    a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
    8b         88 88       d8 88       88 8PP""""""" 88          
    "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
     `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
                  88                                             
                  88           
    """
    print(logo)

def menu() -> None:
    """function used to show menu """
    print(" --- Main Menu --- ")
    print("1 - Back to menu")
    print("2 - Add word")
    print("3 - Encrypt word")
    print("4 - Decrypt word")
    print("5 - Save data")
    print("6 - Load data")
    print("7 - Exit program")
    print("8 - Show help")
    print("=================")



def add_word() -> None:
    """function used to write the word that will be encrypted or decrypted"""
    user_word:str = input("Welcome to the program. Give the word you want to encrypt or decrypt: ")
    print(f"The word given by user is: {user_word}")
    add_word.user_word:str = user_word

    #Kiedy tworzymy atrybut funkcji w ten sposób, tworzymy nowe miejsce do przechowywania danych, które jest "przywiązane" do samej funkcji. Dzięki temu: Wartość będzie dostępna nawet po zakończeniu wykonywania funkcji add_word().
    #Inne funkcje, jak encrypt_word(), mogą uzyskać dostęp do tej wartości poprzez odwołanie add_word.user_word. Jest to trik w Pythonie, który pozwala uniknąć używania zmiennych globalnych lub przekazywania parametrów. Funkcje w Pythonie są obiektami pierwszej klasy, więc można dodawać do nich atrybuty, podobnie jak do innych obiektów.
    # W twoim przypadku, gdy użytkownik wprowadzi słowo "toster" w funkcji add_word(), atrybut add_word.user_word będzie przechowywał wartość "toster". Następnie funkcja encrypt_word() może odczytać tę wartość bez konieczności otrzymywania jej jako parametr.
    #return user_word

def encrypt_word() -> None:
    """Coding the word function"""
    shift_number:int = int(input(f"Pls give me the shift number for the word:  {add_word.user_word}"))
    print(f"{shift_number} for the {add_word.user_word}")

    alphabet:str = " " + string.ascii_letters + string.digits + string.punctuation
    #print(alphabet)
    alphabet_list:list[str] = list(alphabet)
    added_word_coded:list = []
    #print(len(alphabet_list))
    shift_number:int = shift_number % len(alphabet_list)

    for char in add_word.user_word:
        if char in alphabet_list:
            old_index:int = alphabet_list.index(char)
            new_index:int = (old_index + shift_number) % len(alphabet_list)
            added_word_coded.append(alphabet_list[new_index])
        else:
            added_word_coded.append(char)

    encrypted_word:str = "".join(added_word_coded)

    print(f"you encrypted {add_word.user_word} to {encrypted_word}")
    encrypt_word.alphabet_list: list[str] = alphabet_list
    encrypt_word.encrypted_word:str = encrypted_word

def decrypt_word() -> None:
    reversed_shift_number: int = int(input(f"Pls give me the shift number for the word {add_word.user_word}"))
    decrypted_word_list:list = []
    for rev_char in add_word.user_word:
        if rev_char in encrypt_word.alphabet_list:
            rev_index:int = encrypt_word.alphabet_list.index(rev_char)
            fin_index:int = (rev_index - reversed_shift_number) % len(encrypt_word.alphabet_list)
            decrypted_word_list.append( encrypt_word.alphabet_list[fin_index])
        else:
            decrypted_word_list.append(rev_char)

    decrypted_word:str = "".join(decrypted_word_list)
    print(f"you decrypted {add_word.user_word} to {decrypted_word}")

    decrypt_word.decrypted_word:str = decrypted_word

def save_data() -> None:
    """Save the current word and its encryption/decryption to a file."""
    filename:str = input("Enter filename to save (e.g. cipher.json): ")

    try:
        data_to_save:dict = {}
        if hasattr(encrypt_word, 'encrypted_word'):
            data_to_save['encrypted_word'] = encrypt_word.encrypted_word
        if hasattr(decrypt_word, 'decrypted_word'):
            data_to_save['decrypted_word'] = decrypt_word.decrypted_word

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data_to_save, f, indent=4)

        print(f"Saved to {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")

def load_data():
    """Load saved word data from a file."""
    filename: str = input("Enter filename to load (e.g. data.json): ")
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            loaded_data = json.load(f)

        if 'original_word' in loaded_data:
            add_word.user_word = loaded_data['original_word']
            print(f"Loaded original word: {add_word.user_word}")

        if 'encrypted_word' in loaded_data:
            encrypt_word.encrypted_word = loaded_data['encrypted_word']
            print(f"Loaded encrypted word: {encrypt_word.encrypted_word}")

        if 'decrypted_word' in loaded_data:
            decrypt_word.decrypted_word = loaded_data['decrypted_word']
            print(f"Loaded decrypted word: {decrypt_word.decrypted_word}")

        print(f"Data loaded successfully from {filename}.")

    except FileNotFoundError:
        print(f"File {filename} not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {filename}.")
    except Exception as e:
        print(f"Unexpected error: {e}")

def exit_program():
    print("The program will nowe exit....")
    exit()

def help():
    """helpfile TBD"""
    pass

def main() -> None:
    """main function"""

    print_logo()


    options: Dict[int:Callable[[], None]] = {
        1: menu,
        2: add_word,
        3: encrypt_word,
        4: decrypt_word,
        5: save_data,
        6: load_data,
        7: exit_program,
        8: help,

    }

    while True:
        menu()
        try:
            user_choice = int(input("Choose your option: "))
        except ValueError:
            print("You have to give me the number..")
            continue
        if user_choice in options:
            options[user_choice]()
        else:
            print("incorrect number")


if __name__ == "__main__":
    main()

