from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import Image, ImageTk

from register import RegisterClass
from dashboard import RMS


class LoginClass:

    def __init__(self, root):

        self.root = root
        self.root.title("Login System")
        self.root.geometry("1000x600+150+80")
        self.root.config(bg="#087e8b")
        self.root.resizable(False, False)

        # =====================================================
        # LEFT SIDE
        # =====================================================

        left_frame = Frame(self.root, bg="#033054")
        left_frame.place(x=0, y=0, width=400, height=600)

        # ===== Clock Image =====
        try:
            self.clock_img = Image.open("images/clock.png")
            self.clock_img = self.clock_img.resize((280, 280))
            self.clock_img = ImageTk.PhotoImage(self.clock_img)

            Label(
                left_frame,
                image=self.clock_img,
                bg="#033054"
            ).place(x=60, y=80)

        except Exception as ex:
            Label(
                left_frame,
                text="Clock Image Not Found",
                font=("goudy old style", 18, "bold"),
                bg="#033054",
                fg="white"
            ).place(x=90, y=200)

        # ===== Project Name =====

        Label(
            left_frame,
            text="Student Result",
            font=("goudy old style", 25, "bold"),
            bg="#033054",
            fg="white"
        ).place(x=80, y=390)

        Label(
            left_frame,
            text="Management System",
            font=("goudy old style", 20, "bold"),
            bg="#033054",
            fg="white"
        ).place(x=70, y=435)

        Label(
            left_frame,
            text="Welcome",
            font=("goudy old style", 18),
            bg="#033054",
            fg="white"
        ).place(x=145, y=480)

        # =====================================================
        # RIGHT SIDE
        # =====================================================

        frame = Frame(self.root, bg="white")
        frame.place(x=400, y=0, width=600, height=600)

        # ===== Title =====

        Label(
            frame,
            text="LOGIN HERE",
            font=("goudy old style", 28, "bold"),
            bg="white",
            fg="#087e8b"
        ).place(x=170, y=70)

        # =====================================================
        # EMAIL
        # =====================================================

        Label(
            frame,
            text="EMAIL ADDRESS",
            font=("goudy old style", 15, "bold"),
            bg="white",
            fg="#333333"
        ).place(x=100, y=160)

        self.var_email = StringVar()

        Entry(
            frame,
            textvariable=self.var_email,
            font=("goudy old style", 15),
            bg="#eeeeee",
            bd=1
        ).place(
            x=100,
            y=195,
            width=400,
            height=40
        )

        # =====================================================
        # PASSWORD
        # =====================================================

        Label(
            frame,
            text="PASSWORD",
            font=("goudy old style", 15, "bold"),
            bg="white",
            fg="#333333"
        ).place(x=100, y=255)

        self.var_password = StringVar()

        Entry(
            frame,
            textvariable=self.var_password,
            font=("goudy old style", 15),
            bg="#eeeeee",
            bd=1,
            show="*"
        ).place(
            x=100,
            y=290,
            width=400,
            height=40
        )

        # =====================================================
        # REGISTER
        # =====================================================

        Button(
            frame,
            text="Register New Account",
            font=("goudy old style", 12, "bold"),
            bg="white",
            fg="#e91e63",
            bd=0,
            cursor="hand2",
            command=self.register_window
        ).place(
            x=100,
            y=350
        )

        # =====================================================
        # FORGOT PASSWORD
        # =====================================================

        Button(
            frame,
            text="Forgot Password?",
            font=("goudy old style", 12, "bold"),
            bg="white",
            fg="#e91e63",
            bd=0,
            cursor="hand2",
            command=self.forgot_password
        ).place(
            x=360,
            y=350
        )

        # =====================================================
        # LOGIN BUTTON
        # =====================================================

        Button(
            frame,
            text="Login",
            font=("goudy old style", 16, "bold"),
            bg="#e91e63",
            fg="white",
            cursor="hand2",
            bd=0,
            command=self.login
        ).place(
            x=100,
            y=410,
            width=180,
            height=45
        )

        # =====================================================
        # CLEAR BUTTON
        # =====================================================

        Button(
            frame,
            text="Clear",
            font=("goudy old style", 16, "bold"),
            bg="#607d8b",
            fg="white",
            cursor="hand2",
            bd=0,
            command=self.clear
        ).place(
            x=320,
            y=410,
            width=180,
            height=45
        )

    # =========================================================
    # REGISTER WINDOW
    # =========================================================

    def register_window(self):

        self.new_win = Toplevel(self.root)
        self.new_obj = RegisterClass(self.new_win)

    # =========================================================
    # LOGIN FUNCTION
    # =========================================================

    def login(self):

        email = self.var_email.get().strip()
        password = self.var_password.get()

        # Email validation
        if email == "":
            messagebox.showerror(
                "Error",
                "Email is required",
                parent=self.root
            )
            return

        # Password validation
        if password == "":
            messagebox.showerror(
                "Error",
                "Password is required",
                parent=self.root
            )
            return

        # Database connection
        con = sqlite3.connect("rms.db")
        cur = con.cursor()

        try:

            cur.execute(
                """
                SELECT * FROM users
                WHERE email=? AND password=?
                """,
                (email, password)
            )

            row = cur.fetchone()

            if row is None:

                messagebox.showerror(
                    "Error",
                    "Invalid Email or Password",
                    parent=self.root
                )

            else:

                messagebox.showinfo(
                    "Success",
                    "Login Successful",
                    parent=self.root
                )

                # Close login window
                self.root.destroy()

                # Open Dashboard
                root = Tk()
                obj = RMS(root)
                root.mainloop()

        except Exception as ex:

            messagebox.showerror(
                "Error",
                f"Error due to {str(ex)}",
                parent=self.root
            )

        finally:

            con.close()

    # =========================================================
    # CLEAR FUNCTION
    # =========================================================

    def clear(self):

        self.var_email.set("")
        self.var_password.set("")

    # =========================================================
    # FORGOT PASSWORD
    # =========================================================

    def forgot_password(self):

        messagebox.showinfo(
            "Forgot Password",
            "Please contact the administrator to reset your password.",
            parent=self.root
        )


# =============================================================
# MAIN
# =============================================================

if __name__ == "__main__":

    root = Tk()
    obj = LoginClass(root)
    root.mainloop()