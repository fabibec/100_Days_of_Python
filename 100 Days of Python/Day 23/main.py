import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "w")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()
    # Check for win
    if player.ycor() >= 280:
        scoreboard.level_up()
        player.reset_start()
        car_manager.level_up()
    # Check for collision
    for car in car_manager.car_list:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()