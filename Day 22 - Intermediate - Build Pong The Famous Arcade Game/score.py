from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super(Score, self).__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self,r_score = 0

