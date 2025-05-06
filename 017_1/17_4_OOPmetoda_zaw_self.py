
class User:
    def __init(self, user_id:int, username:str )->None:
        self.id =user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user:str):
        user.followers += 1
        self.following += 1


def main():
    user_1 = User(135,"Adam")
    user_2 = User(355,"Ewa")
    user_1.follow(user_2)


if __name__ == "__main__":
    main()

