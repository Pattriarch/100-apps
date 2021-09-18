from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x, y)

    def move_up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + 40
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 40
            self.goto(self.xcor(), new_y)


class ComputerPaddle(Paddle):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move_up_move_down(self):
        while self.ycor() < 240:
            new_y = self.ycor() + 10
            self.goto(self.xcor(), new_y)
        while self.ycor() > -240:
            new_y = self.ycor() - 10
            self.goto(self.xcor(), new_y)
