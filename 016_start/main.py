
from turtle import Turtle, Screen
#
# # class Turtle:
# #     def __str__(self) -> str:
# #         return "I am turtling"
# #
# #
# # timmy = Turtle()
# #
# #
# #
# # print(str(timmy))
#
#
#
# timmy = Turtle()
# print(timmy)
# timmy.color("green")
# timmy.shape("turtle")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# print(my_screen.canvwidth)
# my_screen.exitonclick()


from prettytable import PrettyTable


table = PrettyTable()
print(table)
table.add_column("Pokemon Name", ["Pikachu","Squirtle", "Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align = "l"
print(table)



