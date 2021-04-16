from turtle import Turtle,Screen

# timmy = turtle.Turtle() # creating obj(timmy) from class(turtle)

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("yellow")

timmy.forward(100)
# object.attribute
my_screen = Screen()
print(my_screen.canvheight) #selecting attribute from obj

#object.method
my_screen.exitonclick()



