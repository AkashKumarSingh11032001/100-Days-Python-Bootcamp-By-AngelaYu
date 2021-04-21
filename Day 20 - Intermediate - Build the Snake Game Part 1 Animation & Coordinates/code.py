from turtle import Screen, Turtle, setup

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")

starting_pos = [(0,0),(-20,0),(-40,0)]
# // CREATE SNAKE BODY
for pos in starting_pos:
    snake_body = Turtle("square")
    snake_body.color("white")
    snake_body.goto(pos)








screen.exitonclick()
