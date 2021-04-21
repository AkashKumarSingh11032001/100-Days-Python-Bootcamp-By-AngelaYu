from turtle import Screen, Turtle, setup
import time


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) #// help just like CRT tube

starting_pos = [(0,0),(-20,0),(-40,0)]
snake = []
# // CREATE SNAKE BODY
for pos in starting_pos:
    snake_body = Turtle("square")
    snake_body.color("white")
    snake_body.penup()
    snake_body.goto(pos)
    snake.append(snake_body)


# // SNAKE MOVEMENT
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    for seg in snake:
        seg.forward(20)

    for seg_num in range(len(snake)-1,0,-1):
        new_x = snake[seg_num-1].xcor()
        new_y = snake[seg_num].goto()
        snake[seg_num].goto(new_x,new_y)







screen.exitonclick()
