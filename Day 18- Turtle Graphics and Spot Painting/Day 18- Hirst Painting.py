# from turtle import Turtle, Screen, colormode
# import random

# # import turtle as t

# timmy = Turtle()
# timmy.pensize(10)
# colormode(255)

# ### Random RGB Color Generator ###
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)

#     return (r, g, b)


# ### Main Code ###
# def paint(rows, cols, colors, gap):
#     for i in range(1, rows + 1):
#         for j in range(1, cols + 1):
#             timmy.penup()
#             timmy.color(random.choice(colors))
#             timmy.setpos(i * gap, j * gap)
#             timmy.pendown()
#             timmy.forward(0)
#             timmy.penup()


# list_of_colors = []
# for i in range(31):
#     list_of_colors.append(random_color())

# paint(10, 10, list_of_colors, 20)

# screen = Screen()
# screen.exitonclick()


### Course Solution ###
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [
    (202, 164, 109),
    (238, 240, 245),
    (150, 75, 49),
    (223, 201, 135),
    (52, 93, 124),
    (172, 154, 40),
    (140, 30, 19),
    (133, 163, 185),
    (198, 91, 71),
    (46, 122, 86),
    (72, 43, 35),
    (145, 178, 148),
    (13, 99, 71),
    (233, 175, 164),
    (161, 142, 158),
    (105, 74, 77),
    (55, 46, 50),
    (183, 205, 171),
    (36, 60, 74),
    (18, 86, 90),
    (81, 148, 129),
    (148, 17, 20),
    (14, 70, 64),
    (30, 68, 100),
    (107, 127, 153),
    (174, 94, 97),
    (176, 192, 209),
]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
