from tkinter import simpledialog
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


def calculateResults(student):
    courseworkTotal = sum(student["coursework"])
    overallMark = courseworkTotal + student["exam"]
    percentage = (overallMark / 160) * 100

    if percentage >= 70:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    return courseworkTotal, overallMark, percentage, grade




def viewAllStudents():
    resultWindow = tk.Toplevel(window)
    resultWindow.title("All Student Records")
    resultWindow.geometry("550x500")
    resultWindow.config(bg="#EAF0F6")

    # Create a canvas for scrolling
    canvas = tk.Canvas(resultWindow, bg="#EAF0F6")
    canvas.pack(side="left", fill="both", expand=True)

    # Create scrollbar
    scrollbar = tk.Scrollbar(
        resultWindow,
        orient="vertical",
        command=canvas.yview
    )
    scrollbar.pack(side="right", fill="y")

    canvas.config(yscrollcommand=scrollbar.set)

    # Frame inside the canvas
    recordFrame = tk.Frame(canvas, bg="#EAF0F6")

    canvas.create_window(
        (0, 0),
        window=recordFrame,
        anchor="nw",
        width=530
    )

    totalPercentage = 0

    for student in students:
        coursework, overall, percentage, grade = calculateResults(student)

        totalPercentage += percentage

        record = (
            f"Name: {student['name']}\n"
            f"Student Code: {student['code']}\n"
            f"Coursework: {coursework}/60\n"
            f"Exam: {student['exam']}/100\n"
            f"Overall: {overall}/160\n"
            f"Percentage: {percentage:.2f}%\n"
            f"Grade: {grade}\n"
        )

        label = tk.Label(
            recordFrame,
            text=record,
            justify="left",
            bg="white",
            fg="#243B53",
            font=("Arial", 10),
            relief="solid",
            bd=1,
            padx=10,
            pady=5
        )
        label.pack(anchor="w", fill="x", padx=10, pady=5)

    # Class summary
    if len(students) > 0:
        average = totalPercentage / len(students)

        summary = (
            f"Number of Students: {len(students)}\n"
            f"Class Average: {average:.2f}%"
        )

        summaryLabel = tk.Label(
            recordFrame,
            text=summary,
            font=("Arial", 11, "bold"),
            bg="#243B53",
            fg="white",
            justify="left",
            padx=10,
            pady=10
        )
        summaryLabel.pack(fill="x", padx=10, pady=10)

    # Update scrolling area
    recordFrame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))



def viewIndividualStudent():
    search = simpledialog.askstring(
        "Search Student",
        "Enter student name or student code:"
    )

    if search is None or search.strip() == "":
        return

    found = []

    for student in students:
        if (search.lower() == student["name"].lower()
                or search == student["code"]):
            found.append(student)

    if len(found) > 0:
        student = found[0]
        coursework, overall, percentage, grade = calculateResults(student)

        record = (
            f"Name: {student['name']}\n"
            f"Student Code: {student['code']}\n"
            f"Coursework: {coursework}/60\n"
            f"Exam: {student['exam']}/100\n"
            f"Overall: {overall}/160\n"
            f"Percentage: {percentage:.2f}%\n"
            f"Grade: {grade}"
        )

        resultWindow = tk.Toplevel(window)
        resultWindow.title("Individual Student Record")
        resultWindow.geometry("350x280")
        resultWindow.config(bg="#EAF0F6")

        label = tk.Label(
            resultWindow,
            text=record,
            justify="left",
            font=("Arial", 11),
            bg="white",
            fg="#243B53",
            padx=15,
            pady=15
        )
        label.pack(padx=15, pady=20)

    else:
        tk.messagebox.showinfo(
            "Not Found",
            "Student could not be found."
        )

def displayStudent(student, title):
    resultWindow = tk.Toplevel(window)
    resultWindow.title(title)
    resultWindow.geometry("350x280")
    resultWindow.config(bg="#EAF0F6")

    coursework, overall, percentage, grade = calculateResults(student)

    record = (
        f"Name: {student['name']}\n"
        f"Student Code: {student['code']}\n"
        f"Coursework: {coursework}/60\n"
        f"Exam: {student['exam']}/100\n"
        f"Overall: {overall}/160\n"
        f"Percentage: {percentage:.2f}%\n"
        f"Grade: {grade}"
    )

    label = tk.Label(
        resultWindow,
        text=record,
        justify="left",
        font=("Arial", 11),
        bg="white",
        fg="#243B53",
        padx=15,
        pady=15
    )
    label.pack(padx=15, pady=20)

def showHighest():
    if len(students) == 0:
        return

    highest = max(
        students,
        key=lambda student: calculateResults(student)[1]
    )

    displayStudent(highest, "Highest Student Mark")


def showLowest():
    if len(students) == 0:
        return

    lowest = min(
        students,
        key=lambda student: calculateResults(student)[1]
    )

    displayStudent(lowest, "Lowest Student Mark")




# -------------------------
# Main Menu Design
# -------------------------

window.config(bg="#EAF0F6")

heading = tk.Label(
    window,
    text="STUDENT MANAGER",
    font=("Arial", 22, "bold"),
    bg="#EAF0F6",
    fg="#4992E0"
)
heading.pack(pady=25)

infoLabel = tk.Label(
    window,
    text="Choose an option below:",
    font=("Arial", 11),
    bg="#EAF0F6",
    fg="#2A4B6F"
)
infoLabel.pack(pady=5)

menu = tk.Frame(window, bg="#EAF0F6")
menu.pack(pady=10)

# Menu buttons
buttons = [
    ("1. View All Student Records", viewAllStudents),
    ("2. View Individual Student", viewIndividualStudent),
    ("3. Highest Overall Mark", showHighest),
    ("4. Lowest Overall Mark", showLowest)
]

for text, command in buttons:
    button = tk.Button(
        menu,
        text=text,
        width=30,
        command=command,
        bg="#280F5D",
        fg="white",
        font=("Arial", 10, "bold"),
        relief="flat"
    )
    button.pack(pady=6, ipady=5)

exitButton = tk.Button(
    window,
    text="EXIT",
    width=30,
    command=window.destroy,
    bg="#3C2453",
    fg="white",
    font=("Arial", 10, "bold"),
    relief="flat"
)
exitButton.pack(pady=10, ipady=5)

window.mainloop()
