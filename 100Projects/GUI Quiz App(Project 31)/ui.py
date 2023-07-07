from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            text="This is where the question goes",
            font=FONT,
            fill="black"
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        # Buttons
        true_img = PhotoImage(file="images/true.png")
        self.true = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true.grid(column=0, row=2)
        false_img = PhotoImage(file="images/false.png")
        self.false = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false.grid(column=1, row=2)
        # Question Label
        self.score = Label(text="Score: ", font=("Arial", 14, "bold"), bg=THEME_COLOR)
        self.score.grid(column=1, row=0)
        # Calling the get_next_question function
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text=f"You have reached the end of the quiz. Your Score is: {self.quiz.score}"
            )
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)
