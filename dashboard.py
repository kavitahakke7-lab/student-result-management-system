from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

from course import CourseClass
from student import StudentClass
from result import ResultClass
from report import ReportClass


class RMS:
    def __init__(self, root):

        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.root.resizable(False, False)

        # ==================================================
        # LOGO
        # ==================================================

        self.logo_dash = ImageTk.PhotoImage(
            file="images/logo_p.png"
        )

        title = Label(
            self.root,
            text="Student Result Management System",
            padx=10,
            compound=LEFT,
            image=self.logo_dash,
            font=("goudy old style", 20, "bold"),
            bg="#033054",
            fg="white"
        )

        title.place(
            x=0,
            y=0,
            relwidth=1,
            height=50
        )

        # ==================================================
        # MENU FRAME
        # ==================================================

        M_Frame = LabelFrame(
            self.root,
            text="Menus",
            font=("times new roman", 15),
            bg="white"
        )

        M_Frame.place(
            x=10,
            y=70,
            width=1340,
            height=80
        )

        # ==================================================
        # COURSE BUTTON
        # ==================================================

        btn_course = Button(
            M_Frame,
            text="Course",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.add_course
        )

        btn_course.place(
            x=20,
            y=5,
            width=200,
            height=40
        )

        # ==================================================
        # STUDENT BUTTON
        # ==================================================

        btn_Student = Button(
            M_Frame,
            text="Student",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.add_student
        )

        btn_Student.place(
            x=240,
            y=5,
            width=200,
            height=40
        )

        # ==================================================
        # RESULT BUTTON
        # ==================================================

        btn_Result = Button(
            M_Frame,
            text="Result",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.add_result
        )

        btn_Result.place(
            x=460,
            y=5,
            width=200,
            height=40
        )

        # ==================================================
        # VIEW RESULT BUTTON
        # ==================================================

        btn_View = Button(
            M_Frame,
            text="View Student Result",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.add_report
        )

        btn_View.place(
            x=680,
            y=5,
            width=200,
            height=40
        )

        # ==================================================
        # LOGOUT BUTTON
        # ==================================================

        btn_Logout = Button(
            M_Frame,
            text="Logout",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.logout
        )

        btn_Logout.place(
            x=900,
            y=5,
            width=200,
            height=40
        )

        # ==================================================
        # EXIT BUTTON
        # ==================================================

        btn_Exit = Button(
            M_Frame,
            text="Exit",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.exit_app
        )

        btn_Exit.place(
            x=1120,
            y=5,
            width=200,
            height=40
        )

        # ==================================================
        # CLOCK IMAGE
        # ==================================================

        self.clock_img = Image.open("images/clock.png")

        self.clock_img = self.clock_img.resize(
            (300, 300),
            Image.Resampling.LANCZOS
        )

        self.clock_img = ImageTk.PhotoImage(
            self.clock_img
        )

        self.lbl_clock = Label(
            self.root,
            image=self.clock_img,
            bg="white"
        )

        self.lbl_clock.place(
            x=50,
            y=190,
            width=300,
            height=300
        )

        # ==================================================
        # LEFT SIDE TEXT
        # ==================================================

        lbl_text1 = Label(
            self.root,
            text="Student Result",
            font=("goudy old style", 24, "bold"),
            bg="white",
            fg="#033054"
        )

        lbl_text1.place(
            x=55,
            y=500,
            width=290,
            height=40
        )

        lbl_text2 = Label(
            self.root,
            text="Management System",
            font=("goudy old style", 18, "bold"),
            bg="white",
            fg="#087e8b"
        )

        lbl_text2.place(
            x=35,
            y=540,
            width=330,
            height=35
        )

        # ==================================================
        # BACKGROUND IMAGE
        # ==================================================

        self.bg_img = Image.open("images/bg.png")

        self.bg_img = self.bg_img.resize(
            (920, 350),
            Image.Resampling.LANCZOS
        )

        self.bg_img = ImageTk.PhotoImage(
            self.bg_img
        )

        self.lbl_bg = Label(
            self.root,
            image=self.bg_img
        )

        self.lbl_bg.place(
            x=400,
            y=180,
            width=920,
            height=350
        )

        # ==================================================
        # TOTAL COURSES
        # ==================================================

        self.lbl_course = Label(
            self.root,
            text="Total Courses\n[ 0 ]",
            font=("goudy old style", 20),
            bd=10,
            relief=RIDGE,
            bg="#e43b06",
            fg="white"
        )

        self.lbl_course.place(
            x=400,
            y=530,
            width=300,
            height=100
        )

        # ==================================================
        # TOTAL STUDENTS
        # ==================================================

        self.lbl_Student = Label(
            self.root,
            text="Total Students\n[ 0 ]",
            font=("goudy old style", 20),
            bd=10,
            relief=RIDGE,
            bg="#0676ad",
            fg="white"
        )

        self.lbl_Student.place(
            x=710,
            y=530,
            width=300,
            height=100
        )

        # ==================================================
        # TOTAL RESULTS
        # ==================================================

        self.lbl_Result = Label(
            self.root,
            text="Total Results\n[ 0 ]",
            font=("goudy old style", 20),
            bd=10,
            relief=RIDGE,
            bg="#038074",
            fg="white"
        )

        self.lbl_Result.place(
            x=1020,
            y=530,
            width=300,
            height=100
        )

        # ==================================================
        # FOOTER
        # ==================================================

        footer = Label(
            self.root,
            text="SRMS - Student Result Management System\n"
                 "Contact us for any Technical Issue: 987xxxx01",
            font=("goudy old style", 12),
            bg="#262626",
            fg="white"
        )

        footer.pack(
            side=BOTTOM,
            fill=X
        )

        # ==================================================
        # DATABASE COUNT
        # ==================================================

        self.dashboard_data()

    # ======================================================
    # DASHBOARD DATA
    # ======================================================

    def dashboard_data(self):

        con = sqlite3.connect("rms.db")
        cur = con.cursor()

        try:

            # Total Courses
            cur.execute(
                "SELECT COUNT(*) FROM course"
            )

            total_course = cur.fetchone()[0]

            # Total Students
            cur.execute(
                "SELECT COUNT(*) FROM student"
            )

            total_student = cur.fetchone()[0]

            # Total Results
            cur.execute(
                "SELECT COUNT(*) FROM result"
            )

            total_result = cur.fetchone()[0]

            # Update Course Count
            self.lbl_course.config(
                text=f"Total Courses\n[ {total_course} ]"
            )

            # Update Student Count
            self.lbl_Student.config(
                text=f"Total Students\n[ {total_student} ]"
            )

            # Update Result Count
            self.lbl_Result.config(
                text=f"Total Results\n[ {total_result} ]"
            )

        except Exception as ex:

            messagebox.showerror(
                "Database Error",
                f"Error due to {str(ex)}",
                parent=self.root
            )

        finally:

            con.close()

    # ======================================================
    # COURSE WINDOW
    # ======================================================

    def add_course(self):

        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(
            self.new_win
        )

    # ======================================================
    # STUDENT WINDOW
    # ======================================================

    def add_student(self):

        self.new_win = Toplevel(self.root)
        self.new_obj = StudentClass(
            self.new_win
        )

    # ======================================================
    # RESULT WINDOW
    # ======================================================

    def add_result(self):

        self.new_win = Toplevel(self.root)
        self.new_obj = ResultClass(
            self.new_win
        )

    # ======================================================
    # REPORT WINDOW
    # ======================================================

    def add_report(self):

        self.new_win = Toplevel(self.root)
        self.new_obj = ReportClass(
            self.new_win
        )

    # ======================================================
    # LOGOUT
    # ======================================================

    def logout(self):

        answer = messagebox.askyesno(
            "Logout",
            "Do you want to logout?",
            parent=self.root
        )

        if answer:

            self.root.destroy()

            from login import LoginClass

            root = Tk()

            obj = LoginClass(root)

            root.mainloop()

    # ======================================================
    # EXIT
    # ======================================================

    def exit_app(self):

        answer = messagebox.askyesno(
            "Exit",
            "Do you want to exit?",
            parent=self.root
        )

        if answer:

            self.root.destroy()


# ==========================================================
# MAIN
# ==========================================================

if __name__ == "__main__":

    root = Tk()

    obj = RMS(root)

    root.mainloop()