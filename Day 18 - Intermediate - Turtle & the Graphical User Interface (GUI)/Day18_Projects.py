from turtle import Screen, Shape, Turtle, color
import random
import turtle
from PIL.Image import new
import colorgram

# rgb_color = []
# colors = colorgram.extract("a.jpg",38)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_color.append(new_color)

# print(rgb_color)

def randomcol():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    random_color = (r,g,b)

    return random_color


my_tut = Turtle()
my_tut.dot(20,randomcol())





screen = Screen()
screen.exitonclick()
