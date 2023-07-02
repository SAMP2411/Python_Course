from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmender"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)

# # import turtle
# from turtle import Turtle, Screen

# # import another_module

# # print(another_module.another_variable)
# # timmy = turtle.Turtle()
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(25)
# my_screen = Screen()

# print(my_screen.canvheight)
# my_screen.exitonclick()
