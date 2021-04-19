from turtle import Screen, Shape, Turtle

tut = Turtle()

for i in range(9):
    side = i
    for j in range(side):
        angle = 360/side
        tut.forward(100)
        tut.left(angle)


