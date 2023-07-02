from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInteface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = 0

        self.score_label = Label(
            text=f"Score : {self.score}", bg=THEME_COLOR, fg="white"
        )
        self.question_canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.question_canvas.create_text(
            150, 125, width=280, text="Question", font=("Arial", 20, "italic")
        )
        right_img = PhotoImage(file="./images/true.png")
        wrong_img = PhotoImage(file="./images/false.png")
        self.right_button = Button(
            image=right_img, highlightthickness=0, command=self.ans_true
        )
        self.wrong_button = Button(
            image=wrong_img, highlightthickness=0, command=self.ans_false
        )

        self.score_label.grid(row=0, column=1)
        self.question_canvas.grid(row=1, column=0, columnspan=2, pady=20, padx=20)
        self.right_button.grid(row=2, column=0)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.question_canvas.itemconfig(
                self.question_text, text="You've reached the end of the quiz."
            )
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def ans_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def ans_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.question_canvas.config(bg="green")
        else:
            self.question_canvas.config(bg="red")

        self.timer = self.window.after(1000, self.get_next_question)
