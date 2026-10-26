from tkinter import *
from tkinter import messagebox
import sqlite3


class RegisterClass:

    def __init__(self, root):

        self.root = root
        self.root.title("Register - Student Result Management System")
        self.root.geometry("700x500+300+100")
        self.root.config(bg="#087e8b")
        self.root.resizable(False, False)

        # ===== Main Frame =====
        frame = Frame(
            self.root,
            bg="white"
        )
        frame.place(x=80, y=50, width=540, height=400)

        # ===== Title =====
        title = Label(
            frame,
            text="CREATE NEW ACCOUNT",
            font=("goudy old style", 22, "bold"),
            bg="white",
            fg="#033054"
        )
        title.place(x=120, y=25)

        # ===== Variables =====
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_password = StringVar()
        self.var_confirm = StringVar()

        # ===== Name =====
        Label(
            frame,
            text="Name",
            font=("goudy old style", 15, "bold"),
            bg="white"
        ).place(x=50, y=90)

        Entry(
            frame,
            textvariable=self.var_name,
            font=("goudy old style", 14),
            bg="lightyellow"
        ).place(x=220, y=90, width=250, height=32)

        # ===== Email =====
        Label(
            frame,
            text="Email",
            font=("goudy old style", 15, "bold"),
            bg="white"
        ).place(x=50, y=140)

        Entry(
            frame,
            textvariable=self.var_email,
            font=("goudy old style", 14),
            bg="lightyellow"
        ).place(x=220, y=140, width=250, height=32)

        # ===== Password =====
        Label(
            frame,
            text="Password",
            font=("goudy old style", 15, "bold"),
            bg="white"
        ).place(x=50, y=190)

        Entry(
            frame,
            textvariable=self.var_password,
            font=("goudy old style", 14),
            bg="lightyellow",
            show="*"
        ).place(x=220, y=190, width=250, height=32)

        # ===== Confirm Password =====
        Label(
            frame,
            text="Confirm Password",
            font=("goudy old style", 15, "bold"),
            bg="white"
        ).place(x=50, y=240)

        Entry(
            frame,
            textvariable=self.var_confirm,
            font=("goudy old style", 14),
            bg="lightyellow",
            show="*"
        ).place(x=220, y=240, width=250, height=32)

        # ===== Register Button =====
        Button(
            frame,
            text="Register",
            font=("goudy old style", 15, "bold"),
            bg="#4caf50",
            fg="white",
            cursor="hand2",
            command=self.register
        ).place(x=180, y=300, width=140, height=40)

        # ===== Clear Button =====
        Button(
            frame,
            text="Clear",
            font=("goudy old style", 15, "bold"),
            bg="#607d8b",
            fg="white",
            cursor="hand2",
            command=self.clear
        ).place(x=330, y=300, width=140, height=40)

    # ===== Register Function =====
    def register(self):

        name = self.var_name.get().strip()
        email = self.var_email.get().strip()
        password = self.var_password.get()
        confirm = self.var_confirm.get()

        if name == "":
            messagebox.showerror(
                "Error",
                "Name is required",
                parent=self.root
            )
            return

        if email == "":
            messagebox.showerror(
                "Error",
                "Email is required",
                parent=self.root
            )
            return

        if password == "":
            messagebox.showerror(
                "Error",
                "Password is required",
                parent=self.root
            )
            return

        if confirm == "":
            messagebox.showerror(
                "Error",
                "Confirm Password is required",
                parent=self.root
            )
            return

        if password != confirm:
            messagebox.showerror(
                "Error",
                "Password and Confirm Password do not match",
                parent=self.root
            )
            return

        con = sqlite3.connect("rms.db")
        cur = con.cursor()

        try:

            cur.execute(
                "SELECT * FROM users WHERE email=?",
                (email,)
            )

            row = cur.fetchone()

            if row:
                messagebox.showerror(
                    "Error",
                    "Email already registered",
                    parent=self.root
                )
                return

            cur.execute(
                """
                INSERT INTO users(name, email, password)
                VALUES (?, ?, ?)
                """,
                (name, email, password)
            )

            con.commit()

            messagebox.showinfo(
                "Success",
                "Registration Successful",
                parent=self.root
            )

            self.clear()
            self.root.destroy()

        except Exception as ex:

            messagebox.showerror(
                "Error",
                f"Error due to {str(ex)}",
                parent=self.root
            )

        finally:
            con.close()

    # ===== Clear =====
    def clear(self):

        self.var_name.set("")
        self.var_email.set("")
        self.var_password.set("")
        self.var_confirm.set("")


if __name__ == "__main__":

    root = Tk()
    obj = RegisterClass(root)
    root.mainloop()