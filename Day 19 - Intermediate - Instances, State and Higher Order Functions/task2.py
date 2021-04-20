from turtle import Screen, Shape, Turtle, clear, color
import random
import turtle
import random

my_tut = Turtle()
screen = Screen()


def move_forw():
    my_tut.forward(10)

def move_back():
    my_tut.backward(10)

def move_rot_lef():
    my_tut.left(5)

def move_rot_rig():
    my_tut.right(5)

def clear():
    my_tut.clear()
    my_tut.penup()
    my_tut.home()
    my_tut.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forw)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=move_rot_lef)
screen.onkey(key="d", fun=move_rot_rig)
screen.onkey(key="c",fun=clear)
screen.exitonclick()