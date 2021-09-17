import turtle as t
from turtle import Screen
import random


def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    tim.color(R, G, B)


tim = t.Turtle()
change_color()
tim.pensize(1)
t.colormode(255)


def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tim.speed("fastest")
directions = [90, 180, 270, 360]

def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tim.color(change_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(2)
















screen = Screen()
screen.exitonclick()
