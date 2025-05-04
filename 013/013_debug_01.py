def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got this")


my_function()

from random import randint

dice_images = ["1","2", "3", "4", "5", "6"]
dice_num = randint(0,5)
print(dice_images[dice_num])


#Try except przykład

# age = int(input("How old are U? "))
#
# if age > 18:
#     print(f"You can drive at age {age}")


try:
    age = int(input("How old are U? "))
except ValueError:
    print("You must input integer")
    age = int(input("How old are U? "))

if age > 18:
    print(f"You can drive at age {age}")





import random
import operator


def mutate(a_list: list) -> None:
    b_list: list = []
    new_item:int = 0
    for item in a_list:
        new_item = item * 2
        new_item+= random.randint(1,3)
        new_item = operator.add(new_item, item)
    b_list.append(new_item)
    print(b_list)



mutate([1, 2, 3, 5, 8, 13])
