from paddle import Paddle
import turtle
from turtle import Screen
from score import Score
from ball import Ball
import time

screen = Screen()
screen.colormode(255)
turtle.setup(width=1000, height=600)
turtle.bgcolor("black")
screen.title("Pong Game")

turtle.tracer(0)
score = Score()
ball = Ball()
user_paddle = Paddle(-470, 0)

second_user_paddle = Paddle(470, 0)
score.draw_scores()
score.draw_menu()
turtle.tracer(1)

screen.listen()
screen.onkey(user_paddle.move_up, "Up")
screen.onkey(user_paddle.move_down, "Down")
screen.onkey(second_user_paddle.move_up, "w")
screen.onkey(second_user_paddle.move_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if (ball.xcor() > 450 and ball.distance(second_user_paddle) < 50) or \
            (ball.xcor() < -450 and ball.distance(user_paddle) < 50):
        ball.bounce_x()
        ball.faster()
    if ball.xcor() > 480:
        turtle.tracer(0)
        score.left_user_add_point()
        ball.goal()
        ball.move_speed = 0.03
        turtle.tracer(1)
    if ball.xcor() < -480:
        turtle.tracer(0)
        score.right_user_add_point()
        ball.goal()
        ball.move_speed = 0.03
        turtle.tracer(1)

screen.exitonclick()
