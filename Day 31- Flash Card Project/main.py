from tkinter import *
import pandas, random, time

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
word = {}


# ---------------------------- Functions ----------------------------#
def next_card():
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = random.choice(data)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=word["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    word = random.choice(data)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=word["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    data.remove(word)
    new_dict = pandas.DataFrame(data)
    new_dict.to_csv("data/words_to_learn.csv", index=FALSE)
    next_card()


# ---------------------------- Pandas Setup ----------------------------#

try:
    datas = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    datas = pandas.read_csv("./data/french_words.csv")
finally:
    data = datas.to_dict(orient="records")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="title", font=TITLE_FONT)
word_text = canvas.create_text(400, 263, text="Word", font=WORD_FONT)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(
    text="Start", highlightthickness=0, image=wrong_img, command=next_card
)
right_img = PhotoImage(file="./images/right.png")
right_btn = Button(
    text="Reset", highlightthickness=0, image=right_img, command=is_known
)

canvas.grid(column=0, row=0, columnspan=2)
wrong_btn.grid(column=0, row=1)
right_btn.grid(column=1, row=1)

next_card()

window.mainloop()
