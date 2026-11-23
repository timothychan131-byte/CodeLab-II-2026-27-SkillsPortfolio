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