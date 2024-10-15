import random as r
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen_width, screen_height = screen.window_width() // 2, screen.window_height() // 2

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, 'Up')


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if r.randint(1, 6) == 1:
        car_manager.spawn_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() >= player.finishLine:
        player.reposition()
        scoreboard.update()
        car_manager.next_level()

    car_manager.move_cars()


screen.exitonclick()
