from turtle import Turtle, Screen, colormode
import random

# import turtle as t

colours = [
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
]

timmy = Turtle()
colormode(255)
timmy.shape("turtle")
timmy.color("orange")

### Random RGB Color Generator ###
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)


### Draw Spirograph ###
def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        timmy.speed(100)
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(5)


### Random Walk ###
# move = [0, 90, 180, 270]

# timmy.pensize(6)
# timmy.ht()
# timmy.speed(9)
# while True:
#     # timmy.color(random.choice(colours))
#     timmy.color(random_color())
#     timmy.forward(10)
#     timmy.setheading(random.choice(move))


## Draw Shapes ###
# for i in range(3, 11):
#     tilt = 360 / i
#     timmy.color(random.choice(colours))
#     for j in range(0, i):
#         timmy.right(tilt)
#         timmy.forward(100)


### Draw Dahsed Line ###
# distance = 101
# count = 0
# for i in range(0, distance):
#     timmy.forward(1)
#     if i % 5 == 0:
#         count += 1

#     if count % 2 == 0:
#         timmy.penup()
#     else:
#         timmy.pendown()


#### Draw Square ###
# timmy.forward(100)
# timmy.right(90)

# timmy.forward(100)
# timmy.right(90)

# timmy.forward(100)
# timmy.right(90)

# timmy.forward(100)
# timmy.right(90)


screen = Screen()
screen.exitonclick()
