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



class Student:
    print("Test Class")

root.withdraw()
page1 = Student(student_window)
page1.time()
root.mainloop()
