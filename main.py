from turtle import Turtle
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(725, 491)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

answer_state = screen.textinput(title="What's another state's name?", prompt="").title()
matching_row = data[data.state == answer_state]
# print(matching_row['x'], matching_row['y'])
print(matching_row['state'])

if not matching_row.empty:
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.hideturtle()
    state_name = matching_row['state'].iloc[0]
    state_x = int(matching_row['x'].iloc[0])
    state_y = int(matching_row['y'].iloc[0])

    new_turtle.goto(state_x, state_y)
    new_turtle.write(state_name)



screen.exitonclick()