from turtle import Turtle

FONT = ("Bit5x3", 80, "normal")
ALIGNMENT = "CENTER"


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.color("white")
        self.left_user_score = 0
        self.right_user_score = 0
        self.right(90)

    def draw_menu(self):
        self.penup()
        self.goto(0, 265)
        self.pendown()
        self.pensize(5)
        for i in range(22):
            self.forward(10)
            self.penup()
            self.forward(15)
            self.pendown()

    def draw_scores(self):
        self.penup()
        self.goto(-100, 190)
        self.write(self.left_user_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 190)
        self.pendown()
        self.write(self.right_user_score, align=ALIGNMENT, font=FONT)

    def left_user_add_point(self):
        self.clear()
        self.left_user_score += 1
        self.draw_scores()
        self.draw_menu()

    def right_user_add_point(self):
        self.clear()
        self.right_user_score += 1
        self.draw_scores()
        self.draw_menu()
