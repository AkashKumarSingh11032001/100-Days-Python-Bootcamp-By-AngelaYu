import turtle

screen = turtle.Screen()
screen.title("US States")

img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

def get_mouse_click(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_click())
turtle.mainloop()

screen.exitonclick()