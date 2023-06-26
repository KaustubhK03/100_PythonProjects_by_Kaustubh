import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.listen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.onkey(key="Up", fun=player.go_up)

car = CarManager()

current_score = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.generate_car()
    car.move_car()

    for each_car in car.car_list:
        if each_car.distance(player) < 20:
            current_score.game_over()
            game_is_on = False

    if player.ycor() > 280:
        player.new_level()
        current_score.increase_score()
        current_score.update_score()
        car.increase_car_speed()

screen.exitonclick()
