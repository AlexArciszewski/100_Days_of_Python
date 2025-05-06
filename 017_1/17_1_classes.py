class User:
    def __init__(self):
        print("new user created")

user_1 = User()
user_1.id = "001"
user_1.username = "angela"

print(user_1.username)

user_2 = User()
user_2.id = "002"
user_2.username = "john"

print(user_2.username)