
import tkinter as tk
import os

window = tk.Tk()
window.title("Student Manager")
window.geometry("600x400")
window.resizable(False, False)


def loadStudents():
    filePath = os.path.join(os.path.dirname(__file__), "studentMarks.txt")

    with open(filePath, "r") as file:
        lines = file.readlines()
        
    students = []

    for line in lines[1:]:
        data = line.strip().split(",")

        student = {
            "code": data[0],
            "name": data[1],
            "coursework": [int(data[2]), int(data[3]), int(data[4])],
            "exam": int(data[5])
        }

        students.append(student)

    return students


students = loadStudents()

heading = tk.Label(
    window,
    text="Student Manager",
    font=("Arial", 18, "bold")
)
heading.pack(pady=20)

window.mainloop()
