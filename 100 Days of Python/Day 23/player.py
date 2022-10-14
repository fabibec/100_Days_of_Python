from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        if self.ycor() < 280:
            self.forward(MOVE_DISTANCE)

    def reset_start(self):
        self.goto(STARTING_POSITION)

