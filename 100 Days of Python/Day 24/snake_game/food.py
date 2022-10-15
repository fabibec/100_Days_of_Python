from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.pu()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.setposition(random_x,random_y)

    def refresh(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.setposition(random_x, random_y)
