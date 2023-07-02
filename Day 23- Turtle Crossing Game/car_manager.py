from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle()
            car.shape("square")
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=0.5, stretch_len=1)
            car.setheading(180)
            car.penup()
            car.goto(300, random.randint(-250, 250))
            self.cars.append(car)

    def move_cars(self):
        self.create_cars()
        for block in self.cars:
            block.forward(self.car_speed)

    def reset(self):
        for block in self.cars:
            block.clear()
        self.car_speed += MOVE_INCREMENT
