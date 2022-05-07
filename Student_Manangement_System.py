# ==================imports===================
import sqlite3
from time import strftime
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

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
        # self.update_std_btn.configure(command=self.update_student)

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
        # self.delete_std_btn.configure(command=self.delete_student)

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

        # ================= TREEVIEW ====================
        self.scrollbarx = Scrollbar(student_window, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(student_window, orient=VERTICAL)
        self.tree = ttk.Treeview(student_window)
        self.tree.place(relx=0.307, rely=0.203, width=880, height=550)
        self.tree.configure(
            yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
        )
        self.tree.configure(selectmode="extended")  # Allowing end user to select Multiple Items

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)
        self.scrollbary.place(relx=0.954, rely=0.203, width=22, height=548)
        self.scrollbarx.place(relx=0.307, rely=0.924, width=884, height=22)

        self.tree.configure(
            columns=(
                "Student ID",
                "Name",
                "Sex",
                "Age",
                "Address",
                "College",
                "Year-Level",
                "Contact No.",
            )
        )

        self.tree.heading("Student ID", text="Student ID", anchor=W)
        self.tree.heading("Name", text="Name", anchor=W)
        self.tree.heading("Sex", text="Sex", anchor=W)
        self.tree.heading("Age", text="Age", anchor=W)
        self.tree.heading("Year-Level", text="Year-Level", anchor=W)
        self.tree.heading("College", text="College", anchor=W)
        self.tree.heading("Address", text="Address", anchor=W)
        self.tree.heading("Contact No.", text="Contact No.", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=80)
        self.tree.column("#2", stretch=NO, minwidth=0, width=280)
        self.tree.column("#3", stretch=NO, minwidth=0, width=50)
        self.tree.column("#4", stretch=NO, minwidth=0, width=50)
        self.tree.column("#5", stretch=NO, minwidth=0, width=100)
        self.tree.column("#6", stretch=NO, minwidth=0, width=100)
        self.tree.column("#7", stretch=NO, minwidth=0, width=120)
        self.tree.column("#8", stretch=NO, minwidth=0, width=97)

        self.DisplayData()

    #realtime View data in Treeview if called
    def DisplayData(self):
        cur.execute("SELECT * FROM student_data")
        fetch = cur.fetchall()
        for data in fetch:
            self.tree.insert("", "end", values=(data))

    # for searching the student using the primary key
    def search_student(self):
        val = []
        for i in self.tree.get_children():
            val.append(i)
            for j in self.tree.item(i)["values"]:
                val.append(j)

        try:
            to_search = int(self.search_entry.get())
        except ValueError:
            messagebox.showerror("Oops!!", "Invalid Student ID.", parent=student_window)
        else:
            for search in val:
                if search==to_search:
                    self.tree.selection_set(val[val.index(search)-1])
                    self.tree.focus(val[val.index(search)-1])
                    messagebox.showinfo("Success!!", "Student ID: {} found.".format(self.search_entry.get()), parent=student_window)
                    break
            else: 
                messagebox.showerror("Oops!!", "Student ID: {} not found.".format(self.search_entry.get()), parent=student_window)

    sel = []
    def on_tree_select(self, Event):
        self.sel.clear() 
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)

    def add_student(self):
        global add_window
        global page_add_window
        add_window = Toplevel()
        page_add_window = Add_student(add_window)
        page_add_window.time()
        add_window.mainloop()


    def Exit(self):
        sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=student_window)
        if sure == True:
            student_window.destroy()

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)



# ============   ADD Window       ==============
class Add_student:
    def __init__(self, top=None):
        
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Add Student")

        self.label1 = Label(add_window)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="C:\\Users\\Gigabyte\\Desktop\\2nd SY. 2021-2022\\Advance-OOP\\Final_Project\\img\\AddStudent.png")
        self.label1.configure(image=self.img)

        self.clock = Label(add_window)
        self.clock.place(relx=0.84, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")


    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)



        


root.withdraw()
page1 = Student(student_window)
page1.time()
root.mainloop()
