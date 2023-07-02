from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(clock_timer, text="00:00")
    timer_text.config(text="Timer")
    tick.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    short_break_sec = SHORT_BREAK_MIN * 60
    work_sec = WORK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_min)
        timer_text.config(text="Break", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_text.config(text="Break", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=PINK)
    else:
        countdown(work_sec)
        timer_text.config(text="Work", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    clock_min = math.floor(count / 60)
    clock_sec = count % 60
    if clock_sec < 10:
        clock_sec = f"0{clock_sec}"
    canvas.itemconfig(clock_timer, text=f"{clock_min}:{clock_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        tick.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# The Image Setup
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
clock_timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 50, "bold"))
canvas.grid(column=1, row=1)

# The Timer Label
timer_text = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_text.grid(column=1, row=0)

# The Start Button
start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

# The reset Button
reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)

# The tick mark
tick = Label(bg=YELLOW, fg=GREEN)
tick.grid(column=1, row=3)

window.mainloop()
