import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from Scoreboard import Score


screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Time!")
screen.bgcolor("black")
screen.tracer(0)


l_paddle = Paddle(-350,0)
r_paddle = Paddle(350, 0)
ball = Ball()

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
score = Score()
is_game_on = True
speed_of_game = 0.1
while is_game_on:
    time.sleep(speed_of_game)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddle.

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        speed_of_game -= 0.01

    if ball.distance(r_paddle) > 50 and ball.xcor() > 400:
        ball.home()
        ball.bounce_x()
        score.l_point()
        if speed_of_game > 0.1:
            speed_of_game = 0.1
    if ball.distance(l_paddle) > 50 and ball.xcor() < -400:
        ball.home()
        ball.bounce_x()
        score.r_point()
        if speed_of_game > 0.1:
            speed_of_game = 0.1

screen.exitonclick()