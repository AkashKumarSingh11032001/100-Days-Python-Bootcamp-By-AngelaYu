from turtle import Screen, Shape, Turtle, clear, color
import random
import turtle
import random

is_race_on = False
screen = Screen()
screen.setup(width= 500,height= 400) #scren size
user_bet = screen.textinput(title="Make your Bet", prompt="Which will win the match") #pop-up
print(user_bet)
colors = ["yellow", "blue", "green", "red", "maroon", "violet", "magenta", "purple" ]
y_pos = [-100, -60, -20, 20, 60, 100, 140, 180]


for _ in range(8):
    my_tut = Turtle("turtle")
    my_tut.color(colors[_])
    my_tut.penup()
    my_tut.goto(x=-230,y=y_pos[_])

if user_bet:
    is_race_on = True

while is_race_on:



screen.exitonclick()