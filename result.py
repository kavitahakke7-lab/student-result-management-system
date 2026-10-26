from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3


class ResultClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x600+80+80")
        self.root.config(bg="white")
        self.root.focus_force()

        # ================= VARIABLES =================
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks = StringVar()
        self.var_full_marks = StringVar()

        # ================= TITLE =================
        title = Label(
            self.root,
            text="Add Student Result",
            font=("goudy old style", 24, "bold"),
            bg="#ff9800",
            fg="black"
        )
        title.place(x=10, y=15, width=1180, height=50)

        # ================= RESULT IMAGE =================
        # Image should be inside images folder
        # File name should be result.png

        try:
            self.result_img = Image.open("images/result.png")
            self.result_img = self.result_img.resize(
                (450, 280),
                Image.Resampling.LANCZOS
            )
            self.result_img = ImageTk.PhotoImage(self.result_img)

            self.lbl_result = Label(
                self.root,
                image=self.result_img,
                bg="white"
            )
            self.lbl_result.place(
                x=700,
                y=100,
                width=450,
                height=280
            )

        except Exception as ex:
            messagebox.showerror(
                "Image Error",
                "Please keep result.png inside images folder.\n\n"
                + str(ex),
                parent=self.root
            )

        # ================= SELECT STUDENT =================
        Label(
            self.root,
            text="Select Student",
            font=("goudy old style", 15, "bold"),
            bg="white"
        ).place(x=50, y=100)

        self.cmb_student = ttk.Combobox(
            self.root,
            textvariable=self.var_roll,
            font=("goudy old style", 13),
            state="readonly"
        )
        self.cmb_student.place(
            x=250,
            y=100,
            width=180,
            height=35
        )

        # ================= SEARCH BUTTON =================
        btn_search = Button(
            self.root,
            text="Search",
            font=("goudy old style", 13, "bold"),
            bg="#03a9f4",
            fg="white",
            cursor="hand2",
            command=self.search_student
        )
        btn_search.place(
            x=450,
            y=100,
            width=110,
            height=35
        )

        # ================= NAME =================
        Label(
            self.root,
            text="Name",
            font=("goudy old style", 15, "bold"),
            bg="white"
        ).place(x=50, y=160)

        Entry(
            self.root,
            textvariable=self.var_name,
            font=("goudy old style", 15),
            state="readonly"
        ).place(
            x=250,
            y=160,
            width=310,
            height=35
        )

        # ================= COURSE =================
        Label(
            self.root,
            text="Course",
            font=("goudy old style", 15, "bold"),
            bg="white"
        ).place(x=50, y=220)

        Entry(
            self.root,
            textvariable=self.var_course,
            font=("goudy old style", 15),
            state="readonly"
        ).place(
            x=250,
            y=220,
            width=310,
            height=35
        )

        # ================= MARKS OBTAINED =================
        Label(
            self.root,
            text="Marks Obtained",
            font=("goudy old style", 15, "bold"),
            bg="white"
        ).place(x=50, y=280)

        Entry(
            self.root,
            textvariable=self.var_marks,
            font=("goudy old style", 15),
            bg="lightyellow"
        ).place(
            x=250,
            y=280,
            width=310,
            height=35
        )

        # ================= FULL MARKS =================
        Label(
            self.root,
            text="Full Marks",
            font=("goudy old style", 15, "bold"),
            bg="white"
        ).place(x=50, y=340)

        Entry(
            self.root,
            textvariable=self.var_full_marks,
            font=("goudy old style", 15),
            bg="lightyellow"
        ).place(
            x=250,
            y=340,
            width=310,
            height=35
        )

        # ================= SUBMIT BUTTON =================
        btn_submit = Button(
            self.root,
            text="Submit",
            font=("goudy old style", 15, "bold"),
            bg="#4caf50",
            fg="white",
            cursor="hand2",
            command=self.add
        )
        btn_submit.place(
            x=250,
            y=410,
            width=110,
            height=40
        )

        # ================= CLEAR BUTTON =================
        btn_clear = Button(
            self.root,
            text="Clear",
            font=("goudy old style", 15, "bold"),
            bg="#607d8b",
            fg="white",
            cursor="hand2",
            command=self.clear
        )
        btn_clear.place(
            x=380,
            y=410,
            width=110,
            height=40
        )

        # Load student roll numbers
        self.get_students()

    # ==================================================
    # GET STUDENTS
    # ==================================================
    def get_students(self):

        con = sqlite3.connect("rms.db")
        cur = con.cursor()

        try:
            cur.execute("SELECT roll FROM student")
            rows = cur.fetchall()

            students = []

            for row in rows:
                students.append(row[0])

            self.cmb_student["values"] = students

        except Exception as ex:
            messagebox.showerror(
                "Error",
                f"Error due to {str(ex)}",
                parent=self.root
            )

        finally:
            con.close()

    # ==================================================
    # SEARCH STUDENT
    # ==================================================
    def search_student(self):

        if self.var_roll.get() == "":
            messagebox.showerror(
                "Error",
                "Please select Student",
                parent=self.root
            )
            return

        con = sqlite3.connect("rms.db")
        cur = con.cursor()

        try:
            cur.execute(
                "SELECT name, course FROM student WHERE roll=?",
                (self.var_roll.get(),)
            )

            row = cur.fetchone()

            if row:
                self.var_name.set(row[0])
                self.var_course.set(row[1])

            else:
                messagebox.showerror(
                    "Error",
                    "Student not found",
                    parent=self.root
                )

        except Exception as ex:
            messagebox.showerror(
                "Error",
                f"Error due to {str(ex)}",
                parent=self.root
            )

        finally:
            con.close()

    # ==================================================
    # ADD RESULT
    # ==================================================
    def add(self):

        if self.var_roll.get() == "":
            messagebox.showerror(
                "Error",
                "Please select Student",
                parent=self.root
            )
            return

        if self.var_name.get() == "":
            messagebox.showerror(
                "Error",
                "Please click Search first",
                parent=self.root
            )
            return

        if self.var_marks.get() == "":
            messagebox.showerror(
                "Error",
                "Marks Obtained is required",
                parent=self.root
            )
            return

        if self.var_full_marks.get() == "":
            messagebox.showerror(
                "Error",
                "Full Marks is required",
                parent=self.root
            )
            return

        # Check marks
        try:
            marks = float(self.var_marks.get())
            full_marks = float(self.var_full_marks.get())

            if marks < 0:
                messagebox.showerror(
                    "Error",
                    "Marks cannot be negative",
                    parent=self.root
                )
                return

            if full_marks <= 0:
                messagebox.showerror(
                    "Error",
                    "Full Marks must be greater than 0",
                    parent=self.root
                )
                return

            if marks > full_marks:
                messagebox.showerror(
                    "Error",
                    "Marks Obtained cannot be greater than Full Marks",
                    parent=self.root
                )
                return

        except ValueError:
            messagebox.showerror(
                "Error",
                "Please enter numbers only",
                parent=self.root
            )
            return

        # Database
        con = sqlite3.connect("rms.db")
        cur = con.cursor()

        try:
            # Check whether result already exists
            cur.execute(
                "SELECT * FROM result WHERE roll=?",
                (self.var_roll.get(),)
            )

            row = cur.fetchone()

            if row:
                messagebox.showerror(
                    "Error",
                    "Result already added for this student",
                    parent=self.root
                )

            else:
                cur.execute(
                    """
                    INSERT INTO result
                    (roll, name, course, marks_obtained, full_marks)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_marks.get(),
                        self.var_full_marks.get()
                    )
                )

                con.commit()

                messagebox.showinfo(
                    "Success",
                    "Result Added Successfully",
                    parent=self.root
                )

                self.clear()

        except Exception as ex:
            messagebox.showerror(
                "Error",
                f"Error due to {str(ex)}",
                parent=self.root
            )

        finally:
            con.close()

    # ==================================================
    # CLEAR
    # ==================================================
    def clear(self):

        self.var_roll.set("")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks.set("")
        self.var_full_marks.set("")


# ======================================================
# MAIN
# ======================================================
if __name__ == "__main__":
    root = Tk()
    obj = ResultClass(root)
    root.mainloop()  