import turtle
import pandas

screen = turtle.Screen()
screen.title("US States")

img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

# // CORDINATE BY CLICKING ON SCREEN
# def get_mouse_click(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click)
# turtle.mainloop()

answer_state = screen.textinput(title="State name",prompt="Guess State name?").lower()

