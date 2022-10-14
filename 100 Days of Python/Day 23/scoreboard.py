from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.pu()
        self.goto(-280, 260)
        self.write_level()

    def write_level(self):
        self.clear()
        self.write(f"Level: {self.level}", False, "left", FONT)

    def level_up(self):
        self.level += 1
        self.write_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over!", False, "center", FONT)