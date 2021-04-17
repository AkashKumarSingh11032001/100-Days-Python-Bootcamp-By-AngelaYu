# from turtle import Turtle,Screen

# # timmy = turtle.Turtle() # creating obj(timmy) from class(turtle)

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("yellow")

# timmy.forward(100)
# # object.attribute
# my_screen = Screen()
# print(my_screen.canvheight) #selecting attribute from obj

# #object.method
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Name",["Akash","Sweety","Priya","Shraddha"])
table.add_column("Age",["21","21","21","19"])
table.align = "l"

print(table)






