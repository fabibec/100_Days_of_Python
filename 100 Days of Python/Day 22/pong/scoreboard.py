from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.pu()
        self.left_score = 0
        self.right_score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, False, "center", ("Courier", 80, "bold"))
        self.goto(100, 200)
        self.write(self.right_score, False, "center", ("Courier", 80, "bold"))

    def update_score(self, player):
        if player == "left_score":
            self.left_score += 1
        else:
            self.right_score += 1
        self.write_score()

    def end_game(self):
        winner = ""
        self.goto(0, 0)
        if self.left_score > self.right_score:
            winner = "Left Player"
        else:
            winner = "Right Player"
        self.write(f"{winner} wins !", False, "center", ("Courier", 25, "bold"))
