import string
import random


def main() -> None:
    pass_words = int(input("How many letters you want in your password? "))
    pass_symbols = int(input("How many symbols you want in your password? "))
    pass_numbers = int(input("How many numbers you want in your password? "))

    password: list[str] = []

    letters = list(string.ascii_letters)
    for i in range(pass_words):
        random_letter = random.choice(letters)
        password.append(random_letter)

    numbers = list(string.digits)
    for j in range(pass_numbers):
        random_number = random.choice(numbers)
        password.append(random_number)

    symbols = list('!@#$%^&*()-_=+[]{}|;:,.<>?/')
    for k in range(pass_symbols):
        random_symbol = random.choice(symbols)
        password.append(random_symbol)

    random.shuffle(password)
    py_pass_string = "".join(password)
    print(py_pass_string)


if __name__ == "__main__":
    main()