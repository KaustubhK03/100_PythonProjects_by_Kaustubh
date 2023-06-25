from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=self.l_score, align="center", font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(arg=self.r_score, align="center", font=('Courier', 80, 'normal'))

    def l_score_update(self):
        self.l_score += 1
        self.update_score()

    def r_score_update(self):
        self.r_score += 1
        self.update_score()