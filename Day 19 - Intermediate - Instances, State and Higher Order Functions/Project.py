from turtle import Screen, Shape, Turtle, clear, color
import random
import turtle
import random


screen = Screen()
screen.setup(width= 500,height= 400) #scren size
user_bet = screen.textinput(title="Make your Bet", prompt="Which will win the match") #pop-up
print(user_bet)
colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple" ]
y_pos = [-100, -80, -60, -40, -20, 0, 20 ,40]


for _ in range(8):
    my_tut = Turtle("turtle")
    my_tut.color(colors[_])
    my_tut.penup()
    my_tut.goto(x=-230,y=y_pos[_])


screen.exitonclick()