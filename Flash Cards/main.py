from tkinter import *
import pandas
import random
import time

record = {}
data_as_dict = {}
BACKGROUND_COLOR = "#B1DDC6"
try:
    data_from_csv = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data_from_csv = pandas.read_csv('data/french_words.csv')
    data_as_dict = original_data_from_csv.to_dict(orient = 'records')
else:
    data_as_dict = data_from_csv.to_dict(orient = 'records')


def english_translation():
    canvas.itemconfig(front_of_card, image = back_of_card)
    canvas.itemconfig(title, text = 'English', fill = 'white')
    canvas.itemconfig(first_text, text = record['English'], fill = 'white')


def new_french_word():
    global record, set_timer
    window.after_cancel(set_timer)
    record = random.choice(data_as_dict)
    french_word = record['French']
    canvas.itemconfig(front_of_card, image = white_background)
    canvas.itemconfig(title, text = 'French', fill = 'black')
    canvas.itemconfig(first_text, text = french_word, fill = 'black')
    set_timer = window.after(3000, english_translation)


def words_learned():
    data_as_dict.remove(record)
    data_to_file = pandas.DataFrame(data_as_dict)
    data_to_file.to_csv('data/words_to_learn.csv', index = False)
    new_french_word()


window = Tk()
window.config(padx = 50, pady = 30, bg = BACKGROUND_COLOR)
window.title('Flash Cards')

set_timer = window.after(3000, english_translation)

canvas = Canvas(width = 800, height = 526, highlightthickness= 0, bg = BACKGROUND_COLOR)
white_background = PhotoImage(file ='images/card_front.png')
back_of_card = PhotoImage(file = 'images/card_back.png')
front_of_card = canvas.create_image(405, 263, image = white_background)
title = canvas.create_text(400, 150, text ='Title', font = ('Arial', 40, 'italic'))
first_text = canvas.create_text(400, 263, text = 'Word', font = ('Arial', 60, 'bold'))
canvas.grid(row = 0, column = 0, columnspan = 2, sticky ='ew')

right_image = PhotoImage(file ='images/right.png')
wrong_image = PhotoImage(file ='images/wrong.png')

right_button = Button(image = right_image, highlightthickness= 0, bg = BACKGROUND_COLOR, command = words_learned)
right_button.grid(row = 1, column = 1)

wrong_button = Button(image = wrong_image, highlightthickness= 0, bg = BACKGROUND_COLOR, command = new_french_word)
wrong_button.grid(row = 1, column = 0)

new_french_word()

window.mainloop()
