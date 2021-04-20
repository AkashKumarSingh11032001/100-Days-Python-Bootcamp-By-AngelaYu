from turtle import Screen, Shape, Turtle, color
import random
import turtle
import random

my_tut = Turtle()
turtle.colormode(255)
tut.speed("fastest")

def randomcol():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    random_color = (r,g,b)

    return random_color

my_tut.setheading(225)
my_tut.forward(250)
my_tut.setheading(0)

number_of_dots = 101
for dot_count in range(1,number_of_dots):
    my_tut.dot(20,randomcol())
    my_tut.forward(50)
    
    if dot_count % 10 == 0:
        my_tut.setheading(90)
        my_tut.forward(50)
        my_tut.setheading(180)
        my_tut.forward(500)
        my_tut.setheading(0)
# rgb_color = []
# colors = colorgram.extract("a.jpg",38)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_color.append(new_color)

# print(rgb_color)










screen = Screen()
screen.exitonclick()
