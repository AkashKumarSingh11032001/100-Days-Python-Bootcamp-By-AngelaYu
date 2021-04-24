from turtle import Screen, Turtle

screen = Screen()
screen.title("Pong Game")
screen.setup(width=800,height=600)
screen.bgcolor("black")

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5,stretch_len=1)
paddle.penup()
paddle.goto(350,0)
screen.tracer(0) #// help just like CRT tube

def go_up():
    new_y = paddle.ycor()+20
    paddle.goto(paddle.xcor(),new_y)

def go_down():
    new_y = paddle.ycor()-20
    paddle.goto(paddle.xcor(),new_y)

screen.listen()
screen.update()
screen.onkey(go_up,"Up")
screen.onkey(go_down,"Down")






screen.exitonclick()
