import turtle as t
from food import Food
from scoreboard import Score
import time
from snake import Snake
screen = t.Screen()
screen.setup(height=700, width=700)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Kaustubh's Snake Game")


snake = Snake()
food = Food()
scoreboard = Score()
screen.listen()
current_score = 0
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()
    if snake.head.xcor() > 330 or snake.head.xcor() < -330 or snake.head.ycor() > 340 or snake.head.ycor() < -340:
        game_is_on = False
        scoreboard.game_over()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()
