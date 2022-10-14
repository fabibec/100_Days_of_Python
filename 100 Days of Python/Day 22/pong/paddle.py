from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shapesize(5, 1)
        self.shape("square")
        self.goto(x_pos, y_pos)
        self.color("white")
        self.pu()

    def go_up(self):
        if self.ycor() < 240:
            self.sety(self.ycor() + 50)

    def go_down(self):
        if self.ycor() > -240:
            self.sety(self.ycor() - 50)
