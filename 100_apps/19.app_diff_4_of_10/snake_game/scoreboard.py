from turtle import Turtle

ALIGNMNET = "center"
FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(0, 260)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Scoreboard: {self.score}", align=ALIGNMNET, font=FONT)

    def add_point(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over.", align=ALIGNMNET, font=("Arial", 32, "normal"))
