import tkinter as tk
from tkinter import messagebox
import random

# Main Window
window = tk.Tk()
window.title("Alexa Tell Me a Joke")
window.geometry("400x300")
window.resizable(False, False)

def loadJokes():
    with open("randomJokes.txt", "r") as file:
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

# Heading
heading = tk.Label(window, text="Joke Assistant", font=("Arial", 20, "bold"))
heading.pack(pady=15)

# Joke Setup
joke_label = tk.Label(window, text="Click below to hear a joke!", font=("Arial", 12), wraplength=350)
joke_label.pack(pady=15)

# Punchline
punchline_label = tk.Label(window, text="", font=("Arial", 11), wraplength=350)
punchline_label.pack(pady=10)

# Buttons
tk.Button(window, text="Alexa tell me a Joke", command=tellJoke).pack(pady=5)
tk.Button(window, text="Show Punchline", command=showPunchline).pack(pady=5)
tk.Button(window, text="Next Joke", command=tellJoke).pack(pady=5)
tk.Button(window, text="Quit", command=window.destroy).pack(pady=5)

window.mainloop()