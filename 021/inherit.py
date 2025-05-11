# 
# 
# class Animal:
#     def __init__(self):
#         self.num_eyes = 2
# 
#     def breath(self):
#         print("inhale,exhale")
# 
# 
# class Fish:
# 
#     def swim(self):
#         print("Moving in water")
# 
# nemo = Fish()
# nemo.swim()



class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("inhale,exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()


    def breathe(self):
        super().breathe()
        print("Doing it underwater")

    
    def swim(self):
        print("Moving in water")

max = Animal()
max.breathe() #inhale,exhale
nemo = Fish()
nemo.swim() #Moving in water
print(nemo.num_eyes) #2
nemo.breathe() #inhale,exhale Doing it underwater

