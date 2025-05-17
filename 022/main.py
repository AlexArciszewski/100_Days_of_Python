from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time



screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
#wyłaczenie animacji paletki na starcie
screen.tracer(0)        #trzeba rfreshowac ekran pętlą while

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()



#sterowanie



screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

#petla while do refreshowania
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    #ruch piłki po starcie gry
    ball.move()
    #kolizja pilki ze sciana
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #zderzenie piłki z paletką
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        print("Made contact")
        ball.bounce_x()

    #Detect R paddle misess
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.update_scoreboard()

    #Detect L paddle misess
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.update_scoreboard()

screen.exitonclick()