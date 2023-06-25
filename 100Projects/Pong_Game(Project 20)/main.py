from turtle import Screen, Turtle
from paddle import Paddle
import time
from scoreboard import Scoreboard
from ball import Ball
screen = Screen()
screen.setup(height=600, width=800)
screen.title("Pong")
screen.bgcolor("black")

dotted_position = 0
screen.tracer(0)

for _ in range(40):
    dotted = Turtle("square")
    dotted.color("white")
    dotted.penup()
    dotted.shapesize(0.2, 0.2)
    dotted.goto(0, -285 + dotted_position)
    dotted_position += 15

score = Scoreboard()

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-360, 0))

ball = Ball()
ball.move_ball()


screen.listen()
screen.onkey(fun=right_paddle.go_up, key="Up")
screen.onkey(fun=right_paddle.go_down, key="Down")

screen.onkey(fun=left_paddle.go_up, key="w")
screen.onkey(fun=left_paddle.go_down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_ball()
        score.l_score_update()

    if ball.xcor() < -390:
        ball.reset_ball()
        score.r_score_update()


screen.exitonclick()
