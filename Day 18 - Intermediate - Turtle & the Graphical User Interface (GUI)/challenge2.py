from turtle import Screen, Shape, Turtle

tut = Turtle()

tut.shape("turtle")
tut.color("blue")

for i in range(10):
    tut.forward(20)
    tut.penup()
    tut.forward(5)
    tut.pendown()


screen = Screen()
screen.exitonclick()