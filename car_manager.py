from turtle import Turtle
import random as r

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def spawn_cars(self):
        new_car = Turtle('square')
        new_car.penup()
        new_car.shapesize(1, 2)
        new_car.color(r.choice(COLORS))
        new_car.goto(300, r.randint(-230, 230))
        self.all_cars.append(new_car)

    def move_cars(self):
        for cars in self.all_cars:
            cars.backward(self.car_speed)


    def next_level(self):
        self.car_speed += MOVE_INCREMENT


