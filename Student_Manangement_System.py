# ==================imports===================
import sqlite3
from tkinter import *

# ============================================

root = Tk()
root.geometry("1366x768")
root.title("Intro")
root.resizable(0, 0)

global student_window
global page1
student_window = Toplevel()


#Connection to database
with sqlite3.connect("C:\\Users\\Gigabyte\\Desktop\\2nd SY. 2021-2022\\Advance-OOP\\Final_Project\\Database\\student.db") as db:
    cur = db.cursor()


# ============================ STUDENT WINDOW ====================================
class Student:
     def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Student Management")

        self.window_title = Label(student_window)
        self.window_title.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="C:\\Users\\Gigabyte\\Desktop\\2nd SY. 2021-2022\\Advance-OOP\\Final_Project\\img\\StudentManageMentUI.png")
        self.window_title.configure(image=self.img)

        self.final_project = Label(student_window)
        self.final_project.place(relx=0.046, rely=0.055, width=136, height=30)
        self.final_project.configure(font="-family {Poppins} -size 10")
        self.final_project.configure(foreground="#000000")
        self.final_project.configure(background="#ffffff")
        self.final_project.configure(text="""Final Project""")
        self.final_project.configure(anchor="w")

        self.clock = Label(student_window)
        self.clock.place(relx=0.9, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        self.search_entry = Entry(student_window)
        self.search_entry.place(relx=0.040, rely=0.286, width=240, height=28)
        self.search_entry.configure(font="-family {Poppins} -size 12")
        self.search_entry.configure(relief="flat")



root.withdraw()
page1 = Student(student_window)
page1.time()
root.mainloop()
