def main() -> None:
    print("Welcome to the band generator")
    city = input("Give me the name of the city you grew in: ")
    pet_name = input("Give me the name of your first pet: ")
    band_name = city +" "+ pet_name
    print(f"Your band name is: {band_name}")


if __name__ == "__main__":
    main()