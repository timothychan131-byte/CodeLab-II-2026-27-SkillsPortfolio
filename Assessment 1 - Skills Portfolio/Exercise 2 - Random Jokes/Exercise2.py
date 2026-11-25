import tkinter as tk
from tkinter import messagebox
import random
import os

# Main Window
window = tk.Tk()
window.title("Alexa Tell Me a Joke")
window.geometry("500x500")
window.resizable(False, False)

def loadJokes():
    path = os.path.join(os.path.dirname(__file__), "randomJokes.txt")

    with open(path, "r") as file:
        jokes = file.readlines()

    return [joke.strip() for joke in jokes if "?" in joke]

jokes = loadJokes()
currentJoke = ""

def tellJoke():
    global currentJoke

    currentJoke = random.choice(jokes)
    setup, punchline = currentJoke.split("?", 1)

    joke_label.config(text=setup + "?")
    punchline_label.config(text="")

def showPunchline():
    if currentJoke:
        setup, punchline = currentJoke.split("?", 1)
        punchline_label.config(text=punchline.strip())


# -------------------------
# Main Window Design
# -------------------------

window.config(bg="#EAF0F6")

# Colours
background = "#EAF0F6"
dark_blue = "#243B53"
button_blue = "#2878B5"
white = "#FFFFFF"
text_colour = "#526579"

# Heading
heading = tk.Label(
    window,
    text="JOKE ASSISTANT",
    font=("Arial", 22, "bold"),
    bg=background,
    fg=dark_blue
)
heading.pack(pady=(25, 15))

# Joke Setup
joke_label = tk.Label(
    window,
    text="Click below to hear a joke!",
    font=("Arial", 12),
    wraplength=350,
    bg=white,
    fg=dark_blue,
    width=38,
    height=4,
    relief="solid",
    bd=1
)
joke_label.pack(pady=15)

# Punchline
punchline_label = tk.Label(
    window,
    text="",
    font=("Arial", 11, "bold"),
    wraplength=350,
    bg=background,
    fg=text_colour,
    height=3
)
punchline_label.pack(pady=10)

# Buttons
joke_btn = tk.Button(
    window,
    text="ALEXA, TELL ME A JOKE",
    command=tellJoke,
    width=25,
    bg=button_blue,
    fg=white,
    font=("Arial", 10, "bold"),
    relief="flat"
)
joke_btn.pack(pady=5, ipady=5)

punchline_btn = tk.Button(
    window,
    text="SHOW PUNCHLINE",
    command=showPunchline,
    width=25,
    bg=button_blue,
    fg=white,
    font=("Arial", 10, "bold"),
    relief="flat"
)
punchline_btn.pack(pady=5, ipady=5)

next_btn = tk.Button(
    window,
    text="NEXT JOKE",
    command=tellJoke,
    width=25,
    bg=button_blue,
    fg=white,
    font=("Arial", 10, "bold"),
    relief="flat"
)
next_btn.pack(pady=5, ipady=5)

quit_btn = tk.Button(
    window,
    text="QUIT",
    command=window.destroy,
    width=25,
    bg=dark_blue,
    fg=white,
    font=("Arial", 10, "bold"),
    relief="flat"
)
quit_btn.pack(pady=10, ipady=5)

window.mainloop()