from turtle import Screen, Shape, Turtle, color
import random
import turtle
import random

my_tut = Turtle()
screen = Screen()


def move_forw():
    my_tut.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forw)
screen.exitonclick()