import turtle, pandas

score = 0

screen = turtle.Screen()
screen.title("U. S. States Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


guess_state = screen.textinput(
    title="Guess the State", prompt="Enter first state's name?"
).title()

states_table = pandas.read_csv("50_states.csv")
guess_states = []

while len(guess_state) < 50:
    if guess_state == "Exit":
        break
    guess_states.append(guess_state)
    state = states_table[states_table.state == guess_state]
    show_state = turtle.Turtle()
    show_state.hideturtle()
    show_state.shape("circle")
    show_state.penup()
    xcor = int(state.x)
    ycor = int(state.y)
    show_state.goto(xcor, ycor)
    show_state.write(guess_state)
    score += 1

    guess_state = screen.textinput(
        title=f"{score}/50 States Correct", prompt="What's another state's name?"
    ).title()

left_states = []
# for guesses in guess_states:
#     left_states.append(states_table.state[states_table.state != guesses])

left_states - [state for state in guess_states if state in states_table.state]


data_dict = {
    "States Left": left_states,
}
print(data_dict)
df = pandas.DataFrame(data_dict)
df.to_csv("states_left.csv")
