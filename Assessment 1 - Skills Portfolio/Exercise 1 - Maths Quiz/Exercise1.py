import tkinter as tk
from tkinter import messagebox

import random

# -------------------------
# Functions
# -------------------------

level = 1
level = 2
level = 3

def displayMenu():
    """Shows the difficulty menu."""
    title_label.config(text="DIFFICULTY LEVEL")

def randomInt():
    if level == 1:
        return random.randint(1, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(1000, 9999)

def decideOperation():
    return random.choice(["+", "-"])


def startQuiz(selected):
    global level, score, question, attempt

    level = selected
    score = 0
    question = 0
    attempt = 0

    menu.pack_forget()
    quiz.pack()

    displayProblem()

def displayProblem():
    global num1, num2, answer, attempt

    if question == 10:
        displayResults()
        return

    attempt = 0
    num1 = randomInt()
    num2 = randomInt()
    operation = decideOperation()

    if operation == "+":
        answer = num1 + num2
    else:
        answer = num1 - num2

    question_label.config(text=f"{num1} {operation} {num2} = ?")
    answer_entry.delete(0, tk.END)
    feedback.config(text=f"Question {question + 1}/10")


def isCorrect():
    global score, question, attempt

    try:
        user_answer = int(answer_entry.get())
    except ValueError:
        feedback.config(text="Please enter a number.")
        return

    if user_answer == answer:
        score += 10 if attempt == 0 else 5
        question += 1
        displayProblem()

    elif attempt == 0:
        attempt = 1
        feedback.config(text="Wrong! Try again.")
        answer_entry.delete(0, tk.END)

    else:
        feedback.config(text=f"Wrong! Answer: {answer}")
        question += 1
        window.after(1200, displayProblem)


def displayResults():
    quiz.pack_forget()

    if score >= 90:
        rank = "A+"
    elif score >= 80:
        rank = "A"
    elif score >= 70:
        rank = "B"
    elif score >= 60:
        rank = "C"
    elif score >= 50:
        rank = "D"
    else:
        rank = "F"

    messagebox.showinfo("Results", f"Score: {score}/100\nRank: {rank}")

    if messagebox.askyesno("Play Again?", "Would you like to play again?"):
        displayMenu()
    else:
        window.destroy()


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
    command=lambda: startQuiz(1)
)
easy_btn.pack(pady=5)

# Medium Button
medium_btn = tk.Button(
    window,
    text="2. Medium",
    width=20,
    command=lambda: startQuiz(2)
)
medium_btn.pack(pady=5)

# Hard Button
hard_btn = tk.Button(
    window,
    text="3. Hard",
    width=20,
    command=lambda: startQuiz(3)
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