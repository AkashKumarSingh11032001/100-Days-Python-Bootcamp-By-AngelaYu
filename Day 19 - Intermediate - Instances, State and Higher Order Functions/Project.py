from turtle import Screen, Shape, Turtle, clear, color
import random
import turtle
import random


screen = Screen()
screen.setup(width= 500,height= 400) #scren size
user_bet = screen.textinput(title="Make your Bet", prompt="Which will win the match") #pop-up
print(user_bet)

my_tut = Turtle("turtle")
my_tut.goto(x=-230,y=-100 )


screen.exitonclick()