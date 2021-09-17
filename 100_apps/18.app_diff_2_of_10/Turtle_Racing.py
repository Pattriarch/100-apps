from turtle import Turtle, Screen
import random

game_is_on = False
s = Screen()
s.setup(width=500, height=400)
user_bet = s.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["green", "blue", "purple", "yellow", "red", "orange"]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-225, y=100 - turtle_index * 40)
    all_turtles.append(new_turtle)

if user_bet:
    game_is_on = True

while game_is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            game_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! Color of winner is {winning_color}")
            else:
                print(f"You've lost. Color of winner is {winning_color}")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)




