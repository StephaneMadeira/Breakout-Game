from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-550, 350)
        self.write(self.score, align="center", font=("Courier", 40, "normal"))

    def point(self):
        self.score += 1
        self.update_scoreboard()

    def winner(self):
        self.clear()
        self.goto(0,0)
        self.write("Winner", align="center", font=("Courier", 60, "normal"))