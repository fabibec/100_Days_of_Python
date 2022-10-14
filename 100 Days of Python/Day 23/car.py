from turtle import Turtle

class Car(Turtle):

    def __init__(self, color, start_y, moving_distance):
        super().__init__()
        self.start_y = start_y
        self.moving_distance = moving_distance
        self.pu()
        self.goto(300, self.start_y)
        self.shape("square")
        self.shapesize(1, 2)
        self.color(color)



