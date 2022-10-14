from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.color("white")
        self.pu()
        self.goto(0, 270)
        self.hideturtle()
        self.write(f"Score: {self.score}", False, "center", ('Courier', 20, 'bold'))

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", False, "center", ('Courier', 20, 'bold'))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", False, "center", ('Courier', 20, 'bold'))



