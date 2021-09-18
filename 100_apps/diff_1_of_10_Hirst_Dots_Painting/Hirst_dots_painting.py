import turtle
from turtle import Turtle, Screen
import random

colour_list = ([(201, 164, 112), (152, 75, 50),
                (221, 201, 138), (57, 95, 126),
                (170, 152, 44), (138, 31, 20),
                (135, 163, 183), (196, 94, 75),
                (49, 121, 88), (143, 177, 149),
                (95, 75, 77), (76, 39, 32),
                (164, 146, 157), (16, 98, 71),
                (232, 176, 165), (54, 46, 48),
                (32, 61, 76), (22, 83, 89),
                (182, 204, 176), (141, 22, 25),
                (86, 147, 127), (45, 66, 85),
                (8, 68, 53), (177, 94, 97),
                (222, 177, 182), (109, 128, 151)])

t = Turtle()
turtle.colormode(255)
t.speed("fastest")

for j in range(10):
    t.hideturtle()
    t.penup()
    t.goto(-200, -200+40*j)
    for i in range(10):
        t.dot(20, random.choice(colour_list))
        t.penup()
        t.forward(50)
        t.pendown()












s = Screen()
s.exitonclick()