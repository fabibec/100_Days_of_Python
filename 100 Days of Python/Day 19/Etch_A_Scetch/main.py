from turtle import Turtle, Screen

draw = Turtle()
screen = Screen()


def go_forward():
    draw.forward(20)


def go_back():
    draw.back(20)


def go_clockwise():
    current_angle = draw.tiltangle() + 18
    draw.right(current_angle)


def go_anti_clockwise():
    current_angle = draw.tiltangle() + 18
    draw.left(current_angle)


def clear_start_pos():
    screen.resetscreen()


screen.listen()
screen.onkey(fun=go_forward, key='w')
screen.onkey(fun=go_back, key='s')
screen.onkey(fun=go_clockwise, key='d')
screen.onkey(fun=go_anti_clockwise, key='a')
screen.onkey(fun=clear_start_pos, key='c')
screen.exitonclick()
