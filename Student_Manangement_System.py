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



class Student:
    print("Test Class")

root.withdraw()
page1 = Student(student_window)
page1.time()
root.mainloop()
