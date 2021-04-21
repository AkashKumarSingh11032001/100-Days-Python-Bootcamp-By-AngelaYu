from turtle import Screen, Turtle, setup

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0) #// help just like CRT tube
screen.title("Snake Game")

starting_pos = [(0,0),(-20,0),(-40,0)]
snake = []
# // CREATE SNAKE BODY
for pos in starting_pos:
    snake_body = Turtle("square")
    snake_body.color("white")
    snake_body.penup()
    snake_body.goto(pos)
    snake.append(snake_body)

screen.update()
# // SNAKE MOVEMENT
game_on = True
while game_on:
    for seg in snake:
        seg.forward(10)







screen.exitonclick()
