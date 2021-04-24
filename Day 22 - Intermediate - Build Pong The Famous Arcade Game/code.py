from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.title("Pong Game")
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.tracer(0) #// help just like CRT tube

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # // Collision with Wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # // Collision with Paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
        print("con")




screen.exitonclick()
