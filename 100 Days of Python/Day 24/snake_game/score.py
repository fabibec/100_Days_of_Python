from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        self.score = 0
        self.highscore = self.get_highscore()
        super().__init__()
        self.color("white")
        self.pu()
        self.goto(0, 270)
        self.hideturtle()
        self.write(f"Score: {self.score} | High Score: {self.highscore}", False, "center", ('Courier', 20, 'bold'))

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.highscore}", False, "center", ('Courier', 20, 'bold'))

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.update_highscore()
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def get_highscore(self):
        with open("data.txt") as file:
            return int(file.read())

    def update_highscore(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.highscore))


