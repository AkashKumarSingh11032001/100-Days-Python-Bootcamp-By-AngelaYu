from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.scores = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()



    def update_score(self):
        self.clear()
        self.write(f"Score: {self.scores}, High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.scores += 1
        self.update_score()

    def reset(self):
        if self.scores > self.high_score:
            self.high_score = self.scores
        self.scores = 0
        self.update_score()

    # def gameOver(self):
    #     self.goto(0,0)
    #     self.write("G A M E  O V E R", align="center", font=("Arial", 24, "normal"))
