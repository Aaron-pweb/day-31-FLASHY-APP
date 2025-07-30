import tkinter
import pandas
import random

#create window
window = tkinter.Tk()

#constances

IMAGE1 = tkinter.PhotoImage(file='wrong.png')
IMAGE2 = tkinter.PhotoImage(file="right.png")
IMAGE3 = tkinter.PhotoImage(file='card_back.png')
IMAGE4 = tkinter.PhotoImage(file="card_front.png")
BACKGROUND_COLOR = "#B1DDC6"
#READING DATA
current_dict = {}
to_learn = {}
try:
    data = pandas.read_csv('words_to_learn.csv')
except FileNotFoundError:
    file = pandas.read_csv('french_words.csv')
    to_learn = file.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_dict, flip_timer
    window.after_cancel(flip_timer)
    current_dict = random.choice(to_learn)
    text = current_dict["French"]
    front_canvas.itemconfig(lang, text="French", fill="black")
    front_canvas.itemconfig(word, text=text, fill="black")
    front_canvas.itemconfig(front_image, image=IMAGE4)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    front_canvas.itemconfig(lang, text="English", fill="white")
    front_canvas.itemconfig(word, text=current_dict["English"], fill="white")
    front_canvas.itemconfig(front_image, image=IMAGE3)
def is_known():
    global to_learn
    to_learn.remove(current_dict)
    original_file = pandas.DataFrame(to_learn)
    original_file.to_csv('data/words_to_learn.csv', index=False)
    next_card()

window.title("Eng ~ Fra Flash")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR, highlightthickness= 0)
flip_timer = window.after(3000, flip_card)

front_canvas = tkinter.Canvas(width=800, height=526, highlightthickness=0)
front_canvas.config(bg=BACKGROUND_COLOR)
front_image = front_canvas.create_image(400, 263, image=IMAGE4)

lang = front_canvas.create_text(400, 150, text='', font=("Arial", 40, "italic"), fill="black")
word = front_canvas.create_text(400, 300, text='', font=("Arial", 60, "bold"), fill="black")
front_canvas.grid(column=0, row=0, columnspan=2)

right_button = tkinter.Button(image=IMAGE2, highlightthickness=0, bg= BACKGROUND_COLOR, command=is_known)
right_button.grid(row=1, column=1)

left_button = tkinter.Button(image=IMAGE1, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
left_button.grid(row=1, column=0)

next_card()
#keep the window open
window.mainloop()

