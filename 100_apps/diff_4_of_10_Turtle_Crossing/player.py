from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.level_passed()
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_left(self):
        if self.xcor() > -290:
            new_x = self.xcor() - 10
            self.goto(new_x, self.ycor())

    def move_right(self):
        if self.xcor() < 290:
            new_x = self.xcor() + 10
            self.goto(new_x, self.ycor())

    def level_passed(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
