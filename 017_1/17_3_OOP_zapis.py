class User:

    def __init__(self, user_id:int, user_name:str, age:int) -> None:
        self.id:int = user_id
        self.name:str = user_name
        self.age:int = age


user = User(1234, "Ala_Makota",20)
print(user.id)  #-> 1234
print(user.name)    # -> Ala_Makota
print(user.age)     #-> 20


user2 = User(67898, "Kot_Ali",10)

print(user2.id)  #-> 67898
print(user2.name)    # -> Kot_Ali
print(user2.age)     #-> 10