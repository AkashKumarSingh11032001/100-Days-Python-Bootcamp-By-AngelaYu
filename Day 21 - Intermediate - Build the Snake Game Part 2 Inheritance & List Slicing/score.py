from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.scores = 0
        self.color("white")
        self.penup()
        self.goto(0, 200)
        self.write(f"Score: {self.scores}",align="center", font=("Arial",24,"normal"))
        self.hideturtle()
