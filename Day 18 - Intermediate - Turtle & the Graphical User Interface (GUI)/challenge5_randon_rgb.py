from turtle import Screen, Shape, Turtle
import random
import turtle

tut = Turtle()
turtle.colormode(255)


tut.speed("fastest")
random_angle = [0,90,180,270]
tut.width(10)
# // colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise"]

def randomcol():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    random_color = (r,g,b)

    return random_color



def randomwalk():
    for i in range(200):
        tut.forward(30)
        tut.color(randomcol())
        tut.setheading(random.choice(random_angle))


randomwalk()

screen = Screen()
screen.exitonclick()