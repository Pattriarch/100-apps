import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Creating classes of screen, player, cars and scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Read pressings
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

# Starting game
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move()

    # If player passed level:
    if player.is_at_finish_line():
        scoreboard.level_gone()
        player.level_passed()
        car_manager.level_up()
        scoreboard.leveling_up()
        # Resetting all cars
        for car in car_manager.all_cars:
            car.reset()
            car.penup()
            car.hideturtle()

    # If player hit a car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
