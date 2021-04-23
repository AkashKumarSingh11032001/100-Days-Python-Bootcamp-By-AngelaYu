from turtle import Screen
import time
from snake import Snake
from food import Food


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) #// help just like CRT tube

# // Snake class object
snake = Snake()
food = Food()

# // CREATE SNAKE BODY
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


# // SNAKE MOVEMENT
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # // Collision with food
    if snake.head.distance(food) < 15:
        print("Collided")


    





screen.exitonclick()
