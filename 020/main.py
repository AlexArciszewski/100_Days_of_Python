from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()














#budowanie węża
# segment_1 = Turtle(shape="square")
# segment_1.color("white")
#
# segment_2 = Turtle(shape="square")
# segment_2.color("white")
# segment_2.goto(-20,0)
#
# segment_3 = Turtle(shape="square")
# segment_3.color("white")
# segment_2.goto(-40,0)

#opcja b for loop

#ruszajcy sie waz z 3 kawałków
#screen.tracer(0) #czarny ekran robimy
#segments = []
#starting_positions = [(0, 0), (-20, 0), (-40,0)]
# for position in starting_positions:
#     new_segment = Turtle(shape="square")
#     new_segment.color("white")
# #     new_segment.penup()
# #     new_segment.goto(position)
# #     segments.append(new_segment)
#
#
#
#
# game_on = True
#
# while game_on:
#     screen.update()
#     time.sleep(0.1)  # spowalniam ekran
#     # for seg in segments:
#     #     seg.forward(20) #dodajemy screen update aby wywołać weza zatrzymanego metodą screen.tracer(0)  i metodę time
#     for seg_num in range(len(segments)-1, 0, -1):
#         new_x = segments[seg_num -1].xcor()
#         new_y = segments[seg_num - 1].ycor()
#         segments[seg_num].goto(new_x,new_y)
#     segments[0].forward(20)
#     #segments[0].left(90)
#
# #tworzymy snake class food class scoreboardclass
#
#
#
#
#
#
#
#


