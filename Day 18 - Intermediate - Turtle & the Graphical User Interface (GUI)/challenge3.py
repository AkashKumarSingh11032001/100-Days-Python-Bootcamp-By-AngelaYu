from turtle import Screen, Shape, Turtle

tut = Turtle()

for i in range(3,9):
    angle = 360/i
    for j in range(side):    
        tut.forward(100)
        tut.left(angle)


screen = Screen()
screen.exitonclick()