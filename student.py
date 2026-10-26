from tkinter import *
from tkinter import ttk, messagebox
import sqlite3


class StudentClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x650+80+80")
        self.root.config(bg="white")
        self.root.focus_force()

        # ================= VARIABLES =================
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()
        self.var_a_date = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()
        self.var_search = StringVar()

        # ================= TITLE =================
        title = Label(
            self.root,
            text="Manage Student Details",
            font=("goudy old style", 20, "bold"),
            bg="#033054",
            fg="white"
        )
        title.place(
            x=10,
            y=15,
            width=1180,
            height=35
        )

        # ================= LEFT SIDE LABELS =================

        Label(
            self.root,
            text="Roll No.",
            font=("goudy old style", 15, "bold"),
            bg="white"
        ).place(x=10, y=70)

        Label(
            self.root,
            text="Name",
            font=("goudy old style", 15, "bold"),
            bg="white"
        ).place(x=10, y=110)

        Label(
            self.root,
            text="Email",
            font=("goudy old style", 15, "bold"),
            bg="white"
        ).place(x=10, y=150)

        Label(
            self.root,
            text="Gender",
            font=("goudy old style", 15, "bold"),
            bg="white"
        ).place(x=10, y=190)

        Label(
            self.root,
            text="State",
            font=("goudy old style", 15, "bold"),
            bg="white"
        ).place(x=10, y=230)

        Label(
            self.root,
            text="Address",
            font=("goudy old style", 15, "bold"),
            bg="white"
        ).place(x=10, y=270)

        # ================= LEFT SIDE ENTRY =================

        self.txt_roll = Entry(
            self.root,
            textvariable=self.var_roll,
            font=("goudy old style", 15),
            bg="lightyellow"
        )
        self.txt_roll.place(
            x=150,
            y=70,
            width=200
        )

        Entry(
            self.root,
            textvariable=self.var_name,
            font=("goudy old style", 15),
            bg="lightyellow"
        ).place(
            x=150,
            y=110,
            width=200
        )

        Entry(
            self.root,
            textvariable=self.var_email,
            font=("goudy old style", 15),
            bg="lightyellow"
        ).place(
            x=150,
            y=150,
            width=200
        )

        self.txt_gender = ttk.Combobox(
            self.root,
            textvariable=self.var_gender,
            font=("goudy old style", 15),
            state="readonly",
            justify=CENTER
        )

        self.txt_gender["values"] = (
            "Male",
            "Female",
            "Other"
        )

        self.txt_gender.place(
            x=150,
            y=190,
            width=200
        )

        Entry(
            self.root,
            textvariable=self.var_state,
            font=("goudy old style", 15),
            bg="lightyellow"
        ).place(
            x=150,
            y=230,
            width=200
        )

        self.txt_address = Text(
            self.root,
            font=("goudy old style", 15),
            bg="lightyellow"
        )

        self.txt_address.place(
            x=150,
            y=270,
            width=500,
            height=100
        )

        # ================= RIGHT SIDE LABELS =================

        Label(
            self.root,
            text="D.O.B(dd-mm-yyyy)",
            font=("goudy old style", 15, "bold"),
            bg="white"
        ).place(x=380, y=70)

        Label(
            self.root,
            text="Contact No.",
            font=("goudy old style", 15, "bold"),
            bg="white"
        ).place(x=380, y=110)

        Label(
            self.root,
            text="Select Course",
            font=("goudy old style", 15, "bold"),
            bg="white"
        ).place(x=380, y=150)

        Label(
            self.root,
            text="Admission Date",
            font=("goudy old style", 15, "bold"),
            bg="white"
        ).place(x=380, y=190)

        Label(
            self.root,
            text="City",
            font=("goudy old style", 15, "bold"),
            bg="white"
        ).place(x=380, y=230)

        Label(
            self.root,
            text="Pin Code",
            font=("goudy old style", 15, "bold"),
            bg="white"
        ).place(x=520, y=230)

        # ================= RIGHT SIDE ENTRY =================

        Entry(
            self.root,
            textvariable=self.var_dob,
            font=("goudy old style", 15),
            bg="lightyellow"
        ).place(
            x=540,
            y=70,
            width=200
        )

        Entry(
            self.root,
            textvariable=self.var_contact,
            font=("goudy old style", 15),
            bg="lightyellow"
        ).place(
            x=540,
            y=110,
            width=200
        )

        # ================= COURSE COMBOBOX =================

        self.txt_course = ttk.Combobox(
            self.root,
            textvariable=self.var_course,
            font=("goudy old style", 15),
            state="readonly",
            justify=CENTER
        )

        self.txt_course.place(
            x=540,
            y=150,
            width=200
        )

        self.get_course()

        # ================= ADMISSION DATE =================

        Entry(
            self.root,
            textvariable=self.var_a_date,
            font=("goudy old style", 15),
            bg="lightyellow"
        ).place(
            x=540,
            y=190,
            width=200
        )

        # ================= CITY =================

        Entry(
            self.root,
            textvariable=self.var_city,
            font=("goudy old style", 15),
            bg="lightyellow"
        ).place(
            x=430,
            y=230,
            width=80
        )

        # ================= PIN =================

        Entry(
            self.root,
            textvariable=self.var_pin,
            font=("goudy old style", 15),
            bg="lightyellow"
        ).place(
            x=600,
            y=230,
            width=140
        )

        # ================= BUTTONS =================

        self.btn_add = Button(
            self.root,
            text="Save",
            font=("goudy old style", 15, "bold"),
            bg="#2196f3",
            fg="white",
            cursor="hand2",
            command=self.add
        )

        self.btn_add.place(
            x=150,
            y=390,
            width=110,
            height=40
        )

        self.btn_update = Button(
            self.root,
            text="Update",
            font=("goudy old style", 15, "bold"),
            bg="#4caf50",
            fg="white",
            cursor="hand2",
            command=self.update
        )

        self.btn_update.place(
            x=270,
            y=390,
            width=110,
            height=40
        )

        self.btn_delete = Button(
            self.root,
            text="Delete",
            font=("goudy old style", 15, "bold"),
            bg="#f44336",
            fg="white",
            cursor="hand2",
            command=self.delete
        )

        self.btn_delete.place(
            x=390,
            y=390,
            width=110,
            height=40
        )

        self.btn_clear = Button(
            self.root,
            text="Clear",
            font=("goudy old style", 15, "bold"),
            bg="#607d8b",
            fg="white",
            cursor="hand2",
            command=self.clear
        )

        self.btn_clear.place(
            x=510,
            y=390,
            width=110,
            height=40
        )

        # ================= SEARCH =================

        Label(
            self.root,
            text="Search | Roll No.",
            font=("goudy old style", 15, "bold"),
            bg="white"
        ).place(
            x=780,
            y=60
        )

        Entry(
            self.root,
            textvariable=self.var_search,
            font=("goudy old style", 15),
            bg="lightyellow"
        ).place(
            x=970,
            y=60,
            width=120
        )

        Button(
            self.root,
            text="Search",
            font=("goudy old style", 15, "bold"),
            bg="#03a9f4",
            fg="white",
            cursor="hand2",
            command=self.search
        ).place(
            x=1095,
            y=60,
            width=95,
            height=30
        )

        # ================= TABLE =================

        self.C_Frame = Frame(
            self.root,
            bd=2,
            relief=RIDGE
        )

        self.C_Frame.place(
            x=760,
            y=100,
            width=430,
            height=430
        )

        Scrolly = Scrollbar(
            self.C_Frame,
            orient=VERTICAL
        )

        Scrollx = Scrollbar(
            self.C_Frame,
            orient=HORIZONTAL
        )

        self.StudentTable = ttk.Treeview(
            self.C_Frame,
            columns=(
                "roll",
                "name",
                "email",
                "gender",
                "dob",
                "contact",
                "course",
                "adate",
                "state",
                "city",
                "pin",
                "address"
            ),
            xscrollcommand=Scrollx.set,
            yscrollcommand=Scrolly.set
        )

        Scrollx.pack(
            side=BOTTOM,
            fill=X
        )

        Scrolly.pack(
            side=RIGHT,
            fill=Y
        )

        Scrollx.config(
            command=self.StudentTable.xview
        )

        Scrolly.config(
            command=self.StudentTable.yview
        )

        self.StudentTable.heading(
            "roll",
            text="Roll No."
        )

        self.StudentTable.heading(
            "name",
            text="Name"
        )

        self.StudentTable.heading(
            "email",
            text="Email"
        )

        self.StudentTable.heading(
            "gender",
            text="Gender"
        )

        self.StudentTable.heading(
            "dob",
            text="D.O.B"
        )

        self.StudentTable.heading(
            "contact",
            text="Contact"
        )

        self.StudentTable.heading(
            "course",
            text="Course"
        )

        self.StudentTable.heading(
            "adate",
            text="Admission Date"
        )

        self.StudentTable.heading(
            "state",
            text="State"
        )

        self.StudentTable.heading(
            "city",
            text="City"
        )

        self.StudentTable.heading(
            "pin",
            text="Pin"
        )

        self.StudentTable.heading(
            "address",
            text="Address"
        )

        self.StudentTable["show"] = "headings"

        self.StudentTable.column(
            "roll",
            width=70
        )

        self.StudentTable.column(
            "name",
            width=100
        )

        self.StudentTable.column(
            "email",
            width=150
        )

        self.StudentTable.column(
            "gender",
            width=80
        )

        self.StudentTable.column(
            "dob",
            width=100
        )

        self.StudentTable.column(
            "contact",
            width=100
        )

        self.StudentTable.column(
            "course",
            width=100
        )

        self.StudentTable.column(
            "adate",
            width=100
        )

        self.StudentTable.column(
            "state",
            width=100
        )

        self.StudentTable.column(
            "city",
            width=100
        )

        self.StudentTable.column(
            "pin",
            width=80
        )

        self.StudentTable.column(
            "address",
            width=150
        )

        self.StudentTable.pack(
            fill=BOTH,
            expand=1
        )

        self.StudentTable.bind(
            "<ButtonRelease-1>",
            self.get_data
        )

        self.show()

    # =====================================================
    # GET COURSE LIST
    # =====================================================

    def get_course(self):

        con = sqlite3.connect("rms.db")
        cur = con.cursor()

        try:

            cur.execute(
                "SELECT Name FROM course"
            )

            rows = cur.fetchall()

            course_list = []

            for row in rows:
                course_list.append(row[0])

            self.txt_course["values"] = course_list

        except Exception as ex:

            messagebox.showerror(
                "Error",
                f"Error due to {str(ex)}",
                parent=self.root
            )

        finally:
            con.close()

    # =====================================================
    # ADD STUDENT
    # =====================================================

    def add(self):

        if self.var_roll.get() == "":
            messagebox.showerror(
                "Error",
                "Roll No. is required",
                parent=self.root
            )
            return

        if self.var_name.get() == "":
            messagebox.showerror(
                "Error",
                "Student Name is required",
                parent=self.root
            )
            return

        con = sqlite3.connect("rms.db")
        cur = con.cursor()

        try:

            cur.execute(
                "SELECT * FROM student WHERE roll=?",
                (self.var_roll.get(),)
            )

            row = cur.fetchone()

            if row is not None:

                messagebox.showerror(
                    "Error",
                    "Roll No. already exists",
                    parent=self.root
                )

            else:

                cur.execute("""
                    INSERT INTO student
                    (
                        roll,
                        name,
                        email,
                        gender,
                        dob,
                        contact,
                        course,
                        admission_date,
                        state,
                        city,
                        pin,
                        address
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    self.var_roll.get(),
                    self.var_name.get(),
                    self.var_email.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_contact.get(),
                    self.var_course.get(),
                    self.var_a_date.get(),
                    self.var_state.get(),
                    self.var_city.get(),
                    self.var_pin.get(),
                    self.txt_address.get("1.0", END)
                ))

                con.commit()

                messagebox.showinfo(
                    "Success",
                    "Student Added Successfully",
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

    # =====================================================
    # SHOW DATA
    # =====================================================

    def show(self):

        con = sqlite3.connect("rms.db")
        cur = con.cursor()

        try:

            cur.execute(
                "SELECT * FROM student"
            )

            rows = cur.fetchall()

            self.StudentTable.delete(
                *self.StudentTable.get_children()
            )

            for row in rows:

                self.StudentTable.insert(
                    "",
                    END,
                    values=row
                )

        except Exception as ex:

            messagebox.showerror(
                "Error",
                f"Error due to {str(ex)}",
                parent=self.root
            )

        finally:
            con.close()

    # =====================================================
    # GET DATA
    # =====================================================

    def get_data(self, event):

        selected = self.StudentTable.focus()

        if selected == "":
            return

        row = self.StudentTable.item(
            selected
        )["values"]

        self.var_roll.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_dob.set(row[4])
        self.var_contact.set(row[5])
        self.var_course.set(row[6])
        self.var_a_date.set(row[7])
        self.var_state.set(row[8])
        self.var_city.set(row[9])
        self.var_pin.set(row[10])

        self.txt_address.delete(
            "1.0",
            END
        )

        self.txt_address.insert(
            END,
            row[11]
        )

        self.txt_roll.config(
            state="readonly"
        )

    # =====================================================
    # UPDATE
    # =====================================================

    def update(self):

        if self.var_roll.get() == "":
            messagebox.showerror(
                "Error",
                "Select student from the list first",
                parent=self.root
            )
            return

        con = sqlite3.connect("rms.db")
        cur = con.cursor()

        try:

            cur.execute("""
                UPDATE student SET
                name=?,
                email=?,
                gender=?,
                dob=?,
                contact=?,
                course=?,
                admission_date=?,
                state=?,
                city=?,
                pin=?,
                address=?
                WHERE roll=?
            """, (
                self.var_name.get(),
                self.var_email.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_contact.get(),
                self.var_course.get(),
                self.var_a_date.get(),
                self.var_state.get(),
                self.var_city.get(),
                self.var_pin.get(),
                self.txt_address.get("1.0", END),
                self.var_roll.get()
            ))

            con.commit()

            messagebox.showinfo(
                "Success",
                "Student Updated Successfully",
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

    # =====================================================
    # DELETE
    # =====================================================

    def delete(self):

        if self.var_roll.get() == "":
            messagebox.showerror(
                "Error",
                "Select student from the list first",
                parent=self.root
            )
            return

        op = messagebox.askyesno(
            "Confirm",
            "Do you really want to delete?",
            parent=self.root
        )

        if op:

            con = sqlite3.connect("rms.db")
            cur = con.cursor()

            try:

                cur.execute(
                    "DELETE FROM student WHERE roll=?",
                    (self.var_roll.get(),)
                )

                con.commit()

                messagebox.showinfo(
                    "Delete",
                    "Student deleted successfully",
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

    # =====================================================
    # SEARCH
    # =====================================================

    def search(self):

        con = sqlite3.connect("rms.db")
        cur = con.cursor()

        try:

            cur.execute(
                "SELECT * FROM student WHERE roll LIKE ?",
                ("%" + self.var_search.get() + "%",)
            )

            rows = cur.fetchall()

            self.StudentTable.delete(
                *self.StudentTable.get_children()
            )

            for row in rows:

                self.StudentTable.insert(
                    "",
                    END,
                    values=row
                )

        except Exception as ex:

            messagebox.showerror(
                "Error",
                f"Error due to {str(ex)}",
                parent=self.root
            )

        finally:
            con.close()

    # =====================================================
    # CLEAR
    # =====================================================

    def clear(self):

        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_course.set("")
        self.var_a_date.set("")
        self.var_state.set("")
        self.var_city.set("")
        self.var_pin.set("")
        self.var_search.set("")

        self.txt_address.delete(
            "1.0",
            END
        )

        self.txt_roll.config(
            state=NORMAL
        )

        self.show()


# =========================================================
# MAIN
# =========================================================

if __name__ == "__main__":

    root = Tk()

    obj = StudentClass(root)

    root.mainloop()