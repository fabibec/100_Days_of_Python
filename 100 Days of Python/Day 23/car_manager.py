from turtle import Turtle
from car import Car
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_list = []
        self.current_moving_speed = STARTING_MOVE_DISTANCE
        self.create_cars(0, 1)

    def create_cars(self, min, max):
        for _ in range(random.randint(min, max)):
            new_car = Car(random.choice(COLORS), random.randint(-220, 280), self.current_moving_speed)
            self.car_list.append(new_car)

    def move_cars(self):
        # Move existing Cars
        for car in self.car_list:
            if car.xcor() < -320:
                self.car_list.remove(car)
            new_x = car.xcor() - self.current_moving_speed
            car.goto(new_x, car.ycor())
        # Create random number of new cars
        randnum = random.randint(0, 1)
        if bool(randnum):
            self.create_cars(0, 1)

    def level_up(self):
        self.current_moving_speed = self.current_moving_speed + MOVE_INCREMENT

