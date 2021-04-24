from turtle import Screen, Turtle

screen = Screen()
screen.title("Pong Game")
screen.setup(width=800,height=600)
screen.bgcolor("black")

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5,stretch_len=1)





screen.exitonclick()
