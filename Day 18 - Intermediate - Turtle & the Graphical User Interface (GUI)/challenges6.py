from turtle import Screen, Shape, Turtle
import random
import turtle

tut = Turtle()
turtle.colormode(255)
tut.speed("fastest")


def randomcol():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    random_color = (r,g,b)

    return random_color

for i in range(360):
    r = 100
    tut.color(randomcol())
    tut.circle(r)
    tut.left(2)