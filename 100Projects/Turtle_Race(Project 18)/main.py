import turtle as t
import random
screen = t.Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
colours = ["red", "orange", "yellow", "green", "blue", "violet"]
all_turtles = []

if user_bet:
    is_race_on = True


i = 0
for color in colours:
    new_turtle = t.Turtle(shape="turtle")
    all_turtles.append(new_turtle)
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(-230, -170 + i)
    i += 70


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner.")
            else:
                print(f"You've lost! The {winning_color} is the winner.")
        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()
