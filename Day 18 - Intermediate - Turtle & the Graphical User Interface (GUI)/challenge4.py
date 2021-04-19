from turtle import Screen, Shape, Turtle
import random


tut = Turtle()
tut.speed("fastest")

random_angle = [0,90,180,360]
colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise"]

tut.width(10)
def randomwalk():
    while True:
        tut.forward(50)
        tut.color(random.choice(colors))
        tut.setheading(random.choice(random_angle))


randomwalk()

screen = Screen()
screen.exitonclick()