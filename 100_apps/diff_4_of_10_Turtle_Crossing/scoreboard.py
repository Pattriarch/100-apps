from turtle import Turtle

FONT = ("Courier", 18, "bold")
FONT_ADDITIONAL = ("Courier", 24, "bold")
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-220, 250)
        self.update_scoreboard()

    def leveling_up(self):
        self.level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-220, 250)
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over.", align=ALIGNMENT, font=FONT_ADDITIONAL)

    def level_gone(self):
        self.goto(0, 0)
        self.write(f"Level passed.", align=ALIGNMENT, font=FONT_ADDITIONAL)
