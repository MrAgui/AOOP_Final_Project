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
with sqlite3.connect("C:\\Users\\Gigabyte\\Desktop\\2nd SY. 2021-2022\\Advance-OOP\\FinalProject\\Database\\student.db") as db:
    cur = db.cursor()


# ============================ STUDENT WINDOW ====================================
class Student:
     def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Student Management")

        self.window_title = Label(student_window)
        self.window_title.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="C:\\Users\\Gigabyte\\Desktop\\2nd SY. 2021-2022\\Advance-OOP\\FinalProject\\img\\StudentManageMentUI.png")
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
        # Search BTN
        self.search_std_btn = Button(student_window)
        self.search_std_btn.place(relx=0.232, rely=0.288, width=75, height=22)
        self.search_std_btn.configure(relief="flat")
        self.search_std_btn.configure(overrelief="flat")
        self.search_std_btn.configure(activebackground="#5BB2FE")
        self.search_std_btn.configure(cursor="hand2")
        self.search_std_btn.configure(foreground="#ffffff")
        self.search_std_btn.configure(background="#5BB2FE")
        self.search_std_btn.configure(font="-family {Poppins SemiBold} -size 10")
        self.search_std_btn.configure(borderwidth="0")
        self.search_std_btn.configure(text="""Search""")
        self.search_std_btn.configure(command=self.search_student)
        # Add BTN
        self.add_std_btn = Button(student_window)
        self.add_std_btn.place(relx=0.052, rely=0.426, width=306, height=28)
        self.add_std_btn.configure(relief="flat")
        self.add_std_btn.configure(overrelief="flat")
        self.add_std_btn.configure(activebackground="#5BB2FE")
        self.add_std_btn.configure(cursor="hand2")
        self.add_std_btn.configure(foreground="#ffffff")
        self.add_std_btn.configure(background="#5BB2FE")
        self.add_std_btn.configure(font="-family {Poppins SemiBold} -size 12")
        self.add_std_btn.configure(borderwidth="0")
        self.add_std_btn.configure(text="""Add Student""")
        self.add_std_btn.configure(command=self.add_student)
        # Update BTN
        self.update_std_btn = Button(student_window)
        self.update_std_btn.place(relx=0.052, rely=0.5, width=306, height=28)
        self.update_std_btn.configure(relief="flat")
        self.update_std_btn.configure(overrelief="flat")
        self.update_std_btn.configure(activebackground="#5BB2FE")
        self.update_std_btn.configure(cursor="hand2")
        self.update_std_btn.configure(foreground="#ffffff")
        self.update_std_btn.configure(background="#5BB2FE")
        self.update_std_btn.configure(font="-family {Poppins SemiBold} -size 12")
        self.update_std_btn.configure(borderwidth="0")
        self.update_std_btn.configure(text="""Update Student""")
        self.update_std_btn.configure(command=self.update_student)
        # Delete BTN
        self.delete_std_btn = Button(student_window)
        self.delete_std_btn.place(relx=0.052, rely=0.57, width=306, height=27)
        self.delete_std_btn.configure(relief="flat")
        self.delete_std_btn.configure(overrelief="flat")
        self.delete_std_btn.configure(activebackground="#5BB2FE")
        self.delete_std_btn.configure(cursor="hand2")
        self.delete_std_btn.configure(foreground="#ffffff")
        self.delete_std_btn.configure(background="#5BB2FE")
        self.delete_std_btn.configure(font="-family {Poppins SemiBold} -size 12")
        self.delete_std_btn.configure(borderwidth="0")
        self.delete_std_btn.configure(text="""Delete Student""")
        self.delete_std_btn.configure(command=self.delete_student)
        # Exit BTN
        self.Exit_btn = Button(student_window)
        self.Exit_btn.place(relx=0.135, rely=0.883, width=76, height=21)
        self.Exit_btn.configure(relief="flat")
        self.Exit_btn.configure(overrelief="flat")
        self.Exit_btn.configure(activebackground="#5BB2FE")
        self.Exit_btn.configure(cursor="hand2")
        self.Exit_btn.configure(foreground="#ffffff")
        self.Exit_btn.configure(background="#5BB2FE")
        self.Exit_btn.configure(font="-family {Poppins SemiBold} -size 12")
        self.Exit_btn.configure(borderwidth="0")
        self.Exit_btn.configure(text="""EXIT""")
        self.Exit_btn.configure(command=self.Exit)


root.withdraw()
page1 = Student(student_window)
page1.time()
root.mainloop()
