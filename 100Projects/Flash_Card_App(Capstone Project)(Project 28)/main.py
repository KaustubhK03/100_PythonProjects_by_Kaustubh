import random
import pandas
from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"
FRONT_CARD_BACKGROUND_COLOR = "#FFFFFF"
FRONT_CARD_TEXT_COLOR = "#080202"
current_card = {}
data_lst = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_lst)
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=current_card["German"], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back)


def known_card():
    data_lst.remove(current_card)
    updated_data = pandas.DataFrame(data_lst)
    updated_data.to_csv("data/words_to_learn_in_German.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

try:
    data = pandas.read_csv("data/words_to_learn_in_German.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/German flash csv - Sheet1.csv")
    data_lst = original_data.to_dict(orient="records")
else:
    data_lst = data.to_dict(orient="records")

# Calling the after() method so that we can flip the card after 3 sec
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), fill=FRONT_CARD_TEXT_COLOR)
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"), fill=FRONT_CARD_TEXT_COLOR)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
cross_img = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_img, highlightthickness=0, command=next_card)
cross_button.grid(column=0, row=1)

tick_img = PhotoImage(file="images/right.png")
tick_button = Button(image=tick_img, highlightthickness=0, command=known_card)
tick_button.grid(column=1, row=1)

next_card()

window.mainloop()
