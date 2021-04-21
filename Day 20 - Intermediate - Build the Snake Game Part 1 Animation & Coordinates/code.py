from turtle import Screen, Turtle, setup
import time
from snake import Snake

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) #// help just like CRT tube

starting_pos = [(0,0),(-20,0),(-40,0)]
snake = []
# // CREATE SNAKE BODY



# // SNAKE MOVEMENT
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    





screen.exitonclick()
