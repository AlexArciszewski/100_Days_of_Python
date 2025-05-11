from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)

for i in range(4):
    tim.forward(100)
    tim.right(90)


#aby okno się zatrzymało
screen = Screen()
#wyjście kliknieciem
screen.exitonclick()


