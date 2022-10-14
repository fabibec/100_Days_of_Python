from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.xmove = 20
        self.ymove = 5
        self.move_speed = 0.1

    def bounce_wall(self):
        self.ymove *= -1

    def bounce_paddle(self):
        self.xmove *= -1
        self.move_speed *= 0.9

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def reset_ball(self):
        self.goto(0, 0)
        self.ymove = abs(self.ymove)
        self.move_speed = 0.1


