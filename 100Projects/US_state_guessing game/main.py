import turtle as t
import pandas
FONT = ('Arial', 8, 'normal')
screen = t.Screen()
screen.title("U.S. States Game")
screen.setup(width=736, height=500)
img = "blank_states_img.gif"
screen.addshape(img)
turtle = t.Turtle(img)

states_data = pandas.read_csv("50_states.csv")
guessed_correctly = []

while len(guessed_correctly) < 50:
    user_ans = screen.textinput(title=f"{len(guessed_correctly)}/50 Guessed correctly",
                                prompt="What's another state name?").title()
    if user_ans == "Exit":
        remaining_states = [state for state in states_data["state"].tolist() if state not in guessed_correctly]
        new_data = pandas.DataFrame(remaining_states)
        new_data.to_csv("states_to_learn")
        break
    for each_state in states_data["state"]:
        if user_ans == each_state:
            guessed_correctly.append(user_ans)
            user_ans_row = states_data[states_data["state"] == user_ans]
            xcor = user_ans_row["x"]
            ycor = user_ans_row["y"]
            new_turtle = t.Turtle()
            new_turtle.penup()
            new_turtle.hideturtle()
            new_turtle.goto(int(xcor), int(ycor))
            new_turtle.write(arg=user_ans, align="center", font=FONT)
