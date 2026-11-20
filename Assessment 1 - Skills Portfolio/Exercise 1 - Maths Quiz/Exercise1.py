import tkinter as tk
from tkinter import messagebox

# -------------------------
# Functions
# -------------------------

def displayMenu():
    """Shows the difficulty menu."""
    title_label.config(text="DIFFICULTY LEVEL")


def startQuiz(level):
    """Will start the quiz later."""
    messagebox.showinfo(
        "Difficulty Selected",
        f"You selected {level} difficulty.\n\nQuiz will be added later."
    )


# -------------------------
# Main Window
# -------------------------

window = tk.Tk()
window.title("Maths Quiz")
window.geometry("400x350")
window.resizable(False, False)

# Heading
heading = tk.Label(
    window,
    text="Maths Quiz",
    font=("Arial", 20, "bold")
)
heading.pack(pady=20)

# Instructions
info_label = tk.Label(
    window,
    text="Choose a difficulty level to begin.",
    font=("Arial", 11)
)
info_label.pack(pady=10)

# Difficulty Title
title_label = tk.Label(
    window,
    text="",
    font=("Arial", 14, "bold")
)
title_label.pack(pady=10)

displayMenu()

# Easy Button
easy_btn = tk.Button(
    window,
    text="1. Easy",
    width=20,
    command=lambda: startQuiz("Easy")
)
easy_btn.pack(pady=5)

# Medium Button
medium_btn = tk.Button(
    window,
    text="2. Medium",
    width=20,
    command=lambda: startQuiz("Medium")
)
medium_btn.pack(pady=5)

# Hard Button
hard_btn = tk.Button(
    window,
    text="3. Hard",
    width=20,
    command=lambda: startQuiz("Hard")
)
hard_btn.pack(pady=5)

# Exit Button
exit_btn = tk.Button(
    window,
    text="Exit",
    width=20,
    command=window.quit
)
exit_btn.pack(pady=20)

window.mainloop()