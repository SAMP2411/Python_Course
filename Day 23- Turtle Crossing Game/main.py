import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
carManager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
won = False
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.update_scoreboard()
    carManager.move_cars()
    won = player.check_if_won()
    if won:
        player.start()
        scoreboard.won()
        carManager.reset()

    for block in carManager.cars:
        if block.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
