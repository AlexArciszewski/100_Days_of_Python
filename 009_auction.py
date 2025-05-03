
bid_dict: dict = {}
def print_logo() -> None:
    logo:str = """                                              88  
                                              88  
                                              88  
 ,adPPYb,d8 ,adPPYYba, 8b       d8  ,adPPYba, 88  
a8"    `Y88 ""     `Y8 `8b     d8' a8P_____88 88  
8b       88 ,adPPPPP88  `8b   d8'  8PP"""""""       88  
"8a,   ,d88 88,    ,88   `8b,d8'   "8b,   ,aa 88  
 `"YbbdP"Y8 `"8bbdP"Y8     "8"      `"Ybbd8"' 88  
 aa,    ,88                                       
  "Y8bbdP"  """
    print(logo)
    print("Welcome to the secret auction program.")



def user_register() -> None:

    user_name:str = input("What is your name? ")
    user_bid:float = float(input("What's your bid: $"))
    data:dict = {user_name: user_bid}
    bid_dict.update(data)
    print(data)

def highest_bid() -> None:
    other_user:str = input("are there any other users? y/n ")
    if other_user == "y":
        user_register()
        highest_bid()
    elif other_user == "n":
        max_bid:float = max(bid_dict.values())
        winner:str = None
        for key, value in bid_dict.items():
            if value == max_bid:
                winner = key
                break
        print(f"Auction ended . The winner was: {key}")


        #opcja b
        # winner = max(bid_dict, key=bid_dict.get)
        # print(f"Auction ended . The winner was: {winner}")

    else:
        print("something went wrong program will now exit")


def main() -> None:
    print_logo()
    user_register()
    highest_bid()


if __name__ == "__main__":
    main()

