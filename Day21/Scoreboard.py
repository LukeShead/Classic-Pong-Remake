from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.goto(0,230)
        self.write(arg=f"{self.l_score} : {self.r_score}", align="Center", font=("Arial", 50, "normal"))

        self.hideturtle()

    def l_point(self):
        self.l_score +=1
        self.clear()
        self.write(arg=f"{self.l_score} : {self.r_score}", align="Center", font=("Arial", 50, "normal"))

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.write(arg=f"{self.l_score} : {self.r_score}", align="Center", font=("Arial", 50, "normal"))