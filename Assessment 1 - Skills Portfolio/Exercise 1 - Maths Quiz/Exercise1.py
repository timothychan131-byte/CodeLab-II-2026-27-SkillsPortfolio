import tkinter as tk
from tkinter import messagebox

import random

# -------------------------
# Functions
# -------------------------

level = 1

def displayMenu():
    """Shows the difficulty menu."""
    title_label.config(text="DIFFICULTY LEVEL")
    quiz.pack_forget()
    menu.pack()

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

    # Reset the answer box and button for the new question
    answer_entry.config(state="normal")
    answer_entry.delete(0, tk.END)
    submit_btn.config(text="Submit", command=isCorrect)

    num1 = randomInt()
    num2 = randomInt()
    operation = decideOperation()

    if operation == "+":
        answer = num1 + num2
    else:
        answer = num1 - num2

    question_label.config(text=f"{num1} {operation} {num2} = ?")
    feedback.config(text=f"Question {question + 1}/10")

    answer_entry.focus()



def isCorrect():
    global score, attempt

    try:
        userAnswer = int(answer_entry.get())
    except ValueError:
        feedback.config(
            text="Please enter a number!",
            fg="orange"
        )
        return

    if userAnswer == answer:
        if attempt == 0:
            score += 10
            feedback.config(
                text="Correct! You earned 10 points.",
                fg="green"
            )
        else:
            score += 5
            feedback.config(
                text="Correct! You earned 5 points.",
                fg="green"
            )

        answer_entry.config(state="disabled")
        submit_btn.config(text="Continue", command=continueQuiz)

    else:
        if attempt == 0:
            attempt = 1
            feedback.config(
                text="Incorrect! You have 1 more attempt.",
                fg="red"
            )
            answer_entry.delete(0, tk.END)
        else:
            feedback.config(
                text=f"Incorrect again! The answer was {answer}.",
                fg="red"
            )
            answer_entry.config(state="disabled")
            submit_btn.config(text="Continue", command=continueQuiz)


def continueQuiz():
    global question

    question += 1

    if question <= 10:
        submit_btn.config(text="Submit", command=isCorrect)
        displayProblem()
    else:
        displayResults()



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
window.geometry("500x500")
window.resizable(False, False)
window.config(bg="#EAF0F6")

# Colours
background = "#EAF0F6"
dark_red = "#532424"
button_red = "#B52828"
white = "#FFFFFF"
text_colour = "#A7B6C5"

# Heading
heading = tk.Label(
    window,
    text="MATHS QUIZ",
    font=("Arial", 22, "bold"),
    bg=background,
    fg=dark_red
)
heading.pack(pady=(25, 10))

# Instructions
info_label = tk.Label(
    window,
    text="Choose a difficulty level to begin.",
    font=("Arial", 11),
    bg=background,
    fg=text_colour
)
info_label.pack(pady=10)

# Difficulty Title
title_label = tk.Label(
    window,
    text="SELECT DIFFICULTY",
    font=("Arial", 13, "bold"),
    bg=background,
    fg=dark_red        
)
title_label.pack(pady=10)

menu = tk.Frame(window, bg=background)
menu.pack()

# Easy Button
easy_btn = tk.Button(
    menu,
    text="1. EASY",
    width=22,
    bg=button_red,
    fg=white,
    font=("Arial", 11, "bold"),
    relief="flat",
    command=lambda: startQuiz(1)
)
easy_btn.pack(pady=5, ipady=5)

# Medium Button
medium_btn = tk.Button(
    menu,
    text="2. MEDIUM",
    width=22,
    bg=button_red,
    fg=white,
    font=("Arial", 11, "bold"),
    relief="flat",
    command=lambda: startQuiz(2)
)
medium_btn.pack(pady=5, ipady=5)

# Hard Button
hard_btn = tk.Button(
    menu,
    text="3. HARD",
    width=22,
    bg=button_red,
    fg=white,
    font=("Arial", 11, "bold"),
    relief="flat",
    command=lambda: startQuiz(3)
)
hard_btn.pack(pady=5, ipady=5)

# Exit Button
exit_btn = tk.Button(
    menu,
    text="EXIT",
    width=22,
    bg=dark_red,
    fg=white,
    font=("Arial", 11, "bold"),
    relief="flat",
    command=window.quit
)
exit_btn.pack(pady=15, ipady=5)

# Quiz Screen
quiz = tk.Frame(window, bg=background)

question_label = tk.Label(
    quiz,
    text="",
    font=("Arial", 24, "bold"),
    bg=background,
    fg=dark_red
)
question_label.pack(pady=25)

answer_entry = tk.Entry(
    quiz,
    font=("Arial", 16),
    justify="center",
    relief="solid",
    bd=1
)
answer_entry.pack(pady=10)

submit_btn = tk.Button(
    quiz,
    text="Submit Answer",
    width=22,
    bg=button_red,
    fg=white,
    font=("Arial", 11, "bold"),
    relief="flat",
    command=isCorrect
)
submit_btn.pack(pady=10, ipady=5)

feedback = tk.Label(
    quiz,
    text="",
    font=("Arial", 11, "bold"),
    bg=background,
    fg=dark_red
)
feedback.pack(pady=15)

displayMenu()


window.mainloop()