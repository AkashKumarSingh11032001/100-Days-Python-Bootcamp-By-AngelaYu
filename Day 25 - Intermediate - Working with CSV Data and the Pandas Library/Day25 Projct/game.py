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
guess_state = []
while len(guess_state) < 50:
    data = pandas.read_csv("50_states.csv")
    all_states = data.state.to_list() # // converting to list

    answer_state = screen.textinput(title="State name",prompt="Guess State name?").title()
    print(answer_state)

    if answer_state == "Exit":
        break
    # if user answer present in 50_state

    if answer_state in all_states:
        guess_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(state_data.state.item())


