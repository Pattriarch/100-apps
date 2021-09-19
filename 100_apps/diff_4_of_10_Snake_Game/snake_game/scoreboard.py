from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highest_score.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Scoreboard: {self.score}. Highest score: {self.high_score}",
                   align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highest_score.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # Ready function if we want to stop game after lose
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game over.", align=ALIGNMENT, font=("Arial", 32, "normal"))
