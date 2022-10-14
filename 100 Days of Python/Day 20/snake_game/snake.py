from turtle import Turtle


class Snake:
    def __init__(self):
        self.snake_body = []
        self.start_x = 40

        for _ in range(3):
            snake_body_el = Turtle(shape="square")
            snake_body_el.color("white")
            snake_body_el.pu()
            snake_body_el.goto(x=self.start_x, y=0)
            self.start_x -= 20
            self.snake_body.append(snake_body_el)

        self.head = self.snake_body[0]
        self.head_direction = 0

    def move(self, distance):
        for body_el_num in range(len(self.snake_body) - 1, 0, -1):
            xpos = self.snake_body[body_el_num - 1].xcor()
            ypos = self.snake_body[body_el_num - 1].ycor()
            self.snake_body[body_el_num].goto(xpos, ypos)
        self.snake_body[0].forward(distance)

    def up(self):
        if self.head_direction != 270:
            self.head.setheading(90)
            self.head_direction = 90

    def down(self):
        if self.head_direction != 90:
            self.head.setheading(270)
            self.head_direction = 270

    def left(self):
        if self.head_direction != 0:
            self.head.setheading(180)
            self.head_direction = 180

    def right(self):
        if self.head_direction != 180:
            self.head.setheading(0)
            self.head_direction = 0

    def add_segment(self, position):
        snake_body_el = Turtle(shape="square")
        snake_body_el.color("white")
        snake_body_el.pu()
        snake_body_el.goto(position)
        self.snake_body.append(snake_body_el)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

