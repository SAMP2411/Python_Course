from turtle import Turtle, Screen
import random

is_race_on = False
tim = Turtle()
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# tim = Turtle(shape="turtle")
# tim.penup()
# tim.goto(-230,35)
tim = []
gap = 30
start = (gap / 2) + (gap * 2)
for i in range(6):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(-230, start)
    start -= gap
    tim.append(t)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in tim:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        turtle.forward(random.randint(0, 10))

screen.exitonclick()
