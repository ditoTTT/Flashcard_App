from tkinter import *
import pandas as pd
import random
import csv

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
dict_data = {}
try:
    data = pd.read_csv('day31/data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('day31/data/french_words.csv')
    dict_data = original_data.to_dict(orient='records')
else:
    dict_data = data.to_dict(orient="records")

def gen_french_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card  = random.choice(dict_data)
    canvas.itemconfig(card_title, text = 'French', fill='black')
    canvas.itemconfig(word, text = current_card['French'], fill='black')
    canvas.itemconfig(canv_img, image=old_img)
    flip_timer = window.after(3000, flip_the_card)

def remove_the_word():
    dict_data.remove(current_card)
    data= pd.DataFrame(dict_data)
    data.to_csv('day31/data/words_to_learn.csv', index=False)

    gen_french_word()


def flip_the_card():
    canvas.itemconfig(card_title, text = 'English', fill='white')
    canvas.itemconfig(word, text = current_card['English'], fill='white')
    canvas.itemconfig(canv_img, image=new_img)

window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer =  window.after(3000, flip_the_card)


canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
old_img = PhotoImage(file='day31/images/card_front.png')
new_img = PhotoImage(file='day31/images/card_back.png')
canv_img = canvas.create_image(400,263, image = old_img)
canvas.grid(row=0, column=0, columnspan=2)



card_title = canvas.create_text(400,150,text='', font=('Ariel', 40, 'italic'))
word= canvas.create_text(400,263,text='', font=('Ariel', 60, 'bold'))  

wrong_image = PhotoImage(file="day31/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=gen_french_word)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="day31/images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=remove_the_word)
right_button.grid(row=1, column=1)

gen_french_word()

window.mainloop()


