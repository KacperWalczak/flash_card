from tkinter import *
import os.path
import pandas
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
# timer = ""

# ------------------------------- MECHANISM ----------------------------------------------------- #
if os.path.isfile("data/words_to_learn.csv"):
    df = pandas.read_csv("data/words_to_learn.csv")
else:
    df = pandas.read_csv("data/german_words.csv")
words_to_learn = df.to_dict(orient="records")


def left_to_learn():
    words_to_learn.remove(current_card)
    pandas.DataFrame(words_to_learn).to_csv("data/words_to_learn.csv", index=False)


def draw_card():
    global current_card, timer
    current_card = choice(words_to_learn)
    language = list(current_card.keys())[0]
    canvas.itemconfig(title, text=language, fill='black')
    canvas.itemconfig(word, text=current_card[language], fill='black')
    canvas.itemconfig(card_background, image=card_front)
    window.after_cancel(timer)
    timer = window.after(3000, reverse_card)


def reverse_card():
    language = list(current_card.keys())[1]
    canvas.itemconfig(title, text=language, fill='white')
    canvas.itemconfig(word, text=current_card[language], fill='white')
    canvas.itemconfig(card_background, image=card_back)


# def reset_timer():
#     if not timer == "":
#         window.after_cancel(timer)


# -------------------------------- UI SETUP ----------------------------------------------------- #


window = Tk()
window.title("Flash Cards")
window.config(padx=40, pady=40, background=BACKGROUND_COLOR)

timer = window.after(3000, reverse_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
card_background = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 300, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=1, row=0, columnspan=2)

image_right = PhotoImage(file='images/right.png')
button_right = Button(image=image_right, border=0, background=BACKGROUND_COLOR,
                      command=lambda: [draw_card(), left_to_learn()])
button_right.grid(column=2, row=2)

image_wrong = PhotoImage(file='images/wrong.png')
button_wrong = Button(image=image_wrong, border=0, background=BACKGROUND_COLOR, command=draw_card)
button_wrong.grid(column=1, row=2)

draw_card()
window.mainloop()
