from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def w():
    tim.forward(20)


def s():
    tim.backward(20)


def d():
    tim.right(20)


def a():
    tim.left(20)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=w)
screen.onkey(key="s", fun=s)
screen.onkey(key="d", fun=d)
screen.onkey(key="a", fun=a)
screen.onkey(key="space", fun=clear)
screen.exitonclick()
