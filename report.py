from tkinter import *
from tkinter import ttk, messagebox
import sqlite3


class ReportClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1100x600+120+80")
        self.root.config(bg="white")
        self.root.focus_force()

        # ================= VARIABLES =================
        self.var_search = StringVar()

        # ================= TITLE =================
        title = Label(
            self.root,
            text="View Student Results",
            font=("goudy old style", 20, "bold"),
            bg="#ff9800",
            fg="white"
        )
        title.place(x=20, y=20, width=1060, height=50)

        # ================= SEARCH =================
        lbl_search = Label(
            self.root,
            text="Search By Roll No.",
            font=("goudy old style", 15, "bold"),
            bg="white"
        )
        lbl_search.place(x=300, y=95)

        txt_search = Entry(
            self.root,
            textvariable=self.var_search,
            font=("goudy old style", 15),
            bg="lightyellow"
        )
        txt_search.place(x=500, y=95, width=180, height=35)

        btn_search = Button(
            self.root,
            text="Search",
            font=("goudy old style", 13, "bold"),
            bg="#03a9f4",
            fg="white",
            cursor="hand2",
            command=self.search
        )
        btn_search.place(x=700, y=95, width=100, height=35)

        btn_clear = Button(
            self.root,
            text="Clear",
            font=("goudy old style", 13, "bold"),
            bg="#607d8b",
            fg="white",
            cursor="hand2",
            command=self.clear
        )
        btn_clear.place(x=820, y=95, width=100, height=35)

        # ================= TABLE FRAME =================
        table_frame = Frame(
            self.root,
            bd=2,
            relief=RIDGE,
            bg="white"
        )
        table_frame.place(x=50, y=155, width=1000, height=300)

        # ================= SCROLLBARS =================
        scroll_y = Scrollbar(
            table_frame,
            orient=VERTICAL
        )
        scroll_x = Scrollbar(
            table_frame,
            orient=HORIZONTAL
        )

        # ================= TREEVIEW =================
        self.ReportTable = ttk.Treeview(
            table_frame,
            columns=(
                "roll",
                "name",
                "course",
                "marks",
                "full_marks",
                "percentage"
            ),
            yscrollcommand=scroll_y.set,
            xscrollcommand=scroll_x.set
        )

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.pack(side=BOTTOM, fill=X)

        scroll_y.config(command=self.ReportTable.yview)
        scroll_x.config(command=self.ReportTable.xview)

        # ================= HEADINGS =================
        self.ReportTable.heading(
            "roll",
            text="Roll No"
        )

        self.ReportTable.heading(
            "name",
            text="Name"
        )

        self.ReportTable.heading(
            "course",
            text="Course"
        )

        self.ReportTable.heading(
            "marks",
            text="Marks Obtained"
        )

        self.ReportTable.heading(
            "full_marks",
            text="Total Marks"
        )

        self.ReportTable.heading(
            "percentage",
            text="Percentage"
        )

        # ================= COLUMNS =================
        self.ReportTable.column(
            "roll",
            width=120,
            anchor=CENTER
        )

        self.ReportTable.column(
            "name",
            width=180,
            anchor=CENTER
        )

        self.ReportTable.column(
            "course",
            width=180,
            anchor=CENTER
        )

        self.ReportTable.column(
            "marks",
            width=160,
            anchor=CENTER
        )

        self.ReportTable.column(
            "full_marks",
            width=160,
            anchor=CENTER
        )

        self.ReportTable.column(
            "percentage",
            width=150,
            anchor=CENTER
        )

        self.ReportTable["show"] = "headings"

        self.ReportTable.pack(
            fill=BOTH,
            expand=1
        )

        # ================= TABLE CLICK =================
        self.ReportTable.bind(
            "<ButtonRelease-1>",
            self.get_data
        )

        # ================= DELETE BUTTON =================
        btn_delete = Button(
            self.root,
            text="Delete",
            font=("goudy old style", 15, "bold"),
            bg="#f44336",
            fg="white",
            cursor="hand2",
            command=self.delete
        )
        btn_delete.place(
            x=480,
            y=480,
            width=120,
            height=40
        )

        # ================= SHOW DATA =================
        self.show()

    # ==================================================
    # SHOW ALL RESULTS
    # ==================================================
    def show(self):

        con = sqlite3.connect("rms.db")
        cur = con.cursor()

        try:
            cur.execute(
                "SELECT roll, name, course, marks_obtained, full_marks FROM result"
            )

            rows = cur.fetchall()

            # Clear old data
            self.ReportTable.delete(
                *self.ReportTable.get_children()
            )

            # Insert data
            for row in rows:

                roll = row[0]
                name = row[1]
                course = row[2]
                marks = float(row[3])
                full_marks = float(row[4])

                # Calculate percentage
                percentage = (marks / full_marks) * 100

                self.ReportTable.insert(
                    "",
                    END,
                    values=(
                        roll,
                        name,
                        course,
                        row[3],
                        row[4],
                        f"{percentage:.2f}%"
                    )
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
    # SEARCH RESULT
    # ==================================================
    def search(self):

        if self.var_search.get() == "":
            messagebox.showerror(
                "Error",
                "Please enter Roll No.",
                parent=self.root
            )
            return

        con = sqlite3.connect("rms.db")
        cur = con.cursor()

        try:

            cur.execute(
                """
                SELECT roll, name, course,
                       marks_obtained, full_marks
                FROM result
                WHERE roll=?
                """,
                (self.var_search.get(),)
            )

            row = cur.fetchone()

            # Clear table
            self.ReportTable.delete(
                *self.ReportTable.get_children()
            )

            if row is None:

                messagebox.showerror(
                    "Error",
                    "Result not found",
                    parent=self.root
                )

                self.show()
                return

            roll = row[0]
            name = row[1]
            course = row[2]
            marks = float(row[3])
            full_marks = float(row[4])

            percentage = (marks / full_marks) * 100

            self.ReportTable.insert(
                "",
                END,
                values=(
                    roll,
                    name,
                    course,
                    row[3],
                    row[4],
                    f"{percentage:.2f}%"
                )
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
    # GET SELECTED DATA
    # ==================================================
    def get_data(self, event):

        selected = self.ReportTable.focus()

        if selected == "":
            return

        row = self.ReportTable.item(selected)

        data = row["values"]

        if data:
            self.var_search.set(data[0])

    # ==================================================
    # DELETE RESULT
    # ==================================================
    def delete(self):

        if self.var_search.get() == "":
            messagebox.showerror(
                "Error",
                "Please select a result first",
                parent=self.root
            )
            return

        con = sqlite3.connect("rms.db")
        cur = con.cursor()

        try:

            cur.execute(
                "SELECT * FROM result WHERE roll=?",
                (self.var_search.get(),)
            )

            row = cur.fetchone()

            if row is None:

                messagebox.showerror(
                    "Error",
                    "Result not found",
                    parent=self.root
                )

                return

            confirm = messagebox.askyesno(
                "Confirm",
                "Do you really want to delete this result?",
                parent=self.root
            )

            if confirm:

                cur.execute(
                    "DELETE FROM result WHERE roll=?",
                    (self.var_search.get(),)
                )

                con.commit()

                messagebox.showinfo(
                    "Success",
                    "Result deleted successfully",
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

        self.var_search.set("")
        self.show()


# ======================================================
# MAIN
# ======================================================

if __name__ == "__main__":

    root = Tk()
    obj = ReportClass(root)
    root.mainloop()