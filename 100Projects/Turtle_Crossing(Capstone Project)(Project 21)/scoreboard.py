from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.penup()
        self.hideturtle()
        self.setposition(-270, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Level : {self.current_level}", align="left", font=FONT)

    def increase_score(self):
        self.current_level += 1

    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)
