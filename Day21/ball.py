from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.moving_up = True
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("slowest")
        self.sety(0)
        self.setx(0)
        self.move_x = 10
        self.move_y = 10


    def move(self):
        ball_y = self.ycor() + self.move_y
        ball_x = self.xcor() + self.move_x
        self.goto(ball_x, ball_y)
    #Left over code for another way to implement bouncing. Adding move_x and Move_y then * by -1 is more efficient.
    #But this still works, you still got it working ;).
        # if ball_y > 280:
        #     self.moving_up = False
        #ball_y = self.ycor() - 10
        # if ball_y < -280:
        #     self.moving_up = True
        #ball_x = self.xcor() - 10



    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_x *= -1
