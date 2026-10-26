from tkinter import *
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3

class CourseClass:
    def __init__(self, root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x488+80+170")
        self.root.config(bg="White")
        self.root.focus_force()
    
        #====Title======  
    
        title=Label(self.root,text="Manage Course Details",font=("goudy old style",20,"bold"),bg="#033054",fg="white" )
        title.place(x=10,y=15,relwidth=1180,height=35)
        title.lift
      
       #===variables====
        self.var_course=StringVar()
        self.var_Duration=StringVar()
        self.var_Charges=StringVar()
                
      #====widgets======
        lbl_CourseName=Label(self.root,text="course Name",font=("goudy old style",15,"bold"),bg="White").place(x=10,y=60)
        lbl_Duration=Label(self.root,text="Duration",font=("goudy old style",15,"bold"),bg="White").place(x=10,y=100)
        lbl_Charges=Label(self.root,text="Charges",font=("goudy old style",15,"bold"),bg="White").place(x=10,y=140)
        lbl_Description=Label(self.root,text="Description",font=("goudy old style",15,"bold"),bg="White").place(x=10,y=180)
      #===Entry fields=====
        self.txt_CourseName=Entry(self.root,textvariable=self.var_course,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_CourseName.place(x=150,y=60,width=200)
        txt_Duration=Entry(self.root,textvariable=self.var_Duration,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=150,y=100,width=200)
        txt_Charges=Entry(self.root,textvariable=self.var_Charges,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=150,y=140,width=200)
        self.txt_Description=Text(self.root,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_Description.place(x=150,y=180,width=500,height=130)

       #===buttons=====
         #====Buttons================

        self.btn_add = Button(self.root,text="Save",font=("goudy old style", 15, "bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=150, y=400, width=110, height=40)
        self.btn_update = Button(self.root,text="Update",font=("goudy old style", 15, "bold"),bg="#4caf50",fg="white",cursor="hand2",command=self.Upadate)
        self.btn_update.place(x=270, y=400, width=110, height=40)
        self.btn_delete = Button(self.root,text="Delete",font=("goudy old style", 15, "bold"),bg="#f44336",fg="white",cursor="hand2",command=self.delete )
        self.btn_delete.place(x=390, y=400, width=110, height=40)
        self.btn_clear = Button(self.root,text="Clear",font=("goudy old style", 15, "bold"),bg="#607d8b",fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510, y=400, width=110, height=40) 
        

      #===search panel======
        self.var_Search=StringVar()
        lbl_Search_CourseName=Label(self.root,text="Course Name",font=("goudy old style",15,"bold"),bg="White").place(x=720,y=60)
        self.txt_Search_CourseName=Entry(self.root,textvariable=self.var_Search,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=870,y=60,width=180)
        btn_search = Button(self.root,text="Search",font=("goudy old style", 15, "bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search).place(x=1070, y=60, width=120, height=28)
      #===content=====
       
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=100,width=470,height=340)

        Scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        Scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("cid","Name","Duration","Charges","Description"),xscrollcommand=Scrollx.set,yscrollcommand=Scrolly.set)
       
       
        Scrollx.pack(side=BOTTOM,fill=X)
        Scrolly.pack(side=RIGHT,fill=Y)
        Scrollx.config(command=self.CourseTable.xview)
        Scrolly.config(command=self.CourseTable.yview)

        self.CourseTable.heading("cid",text="Course ID")
        self.CourseTable.heading("Name",text="Name")
        self.CourseTable.heading("Duration",text="Duration")
        self.CourseTable.heading("Charges",text="Charges")
        self.CourseTable.heading("Description",text="Description")
        self.CourseTable["show"]="headings"
        
        self.CourseTable.column("cid",width=50)
        self.CourseTable.column("Name",width=100)
        self.CourseTable.column("Duration",width=100)
        self.CourseTable.column("Charges",width=100)
        self.CourseTable.column("Description",width=150)
        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#=========================================================================================
    def clear(self):
         self.show()
         self.var_course.set("")
         self.var_Duration.set("")
         self.var_Charges.set("")
         self.var_Search.set("")
         #self.var_Desception.set(row[4])
         self.txt_Description.delete('1.0',END)
         self.txt_CourseName.config(state=NORMAL)
    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
             messagebox.showerror("Error","Course Name should be Required",parent=self.root)
            else:
              cur.execute("select * from course where Name=?",(self.var_course.get(),))
              row=cur.fetchone()
              print(row)
              if row==None:
               messagebox.showerror("Error","Please select course from the list first",parent=self.root)
              else: 
                  op=messagebox.askyesno("confirm","Do you really Want to delete?",parent=self.root)
                  if op==True:
                      cur.execute("delete from course where Name=?",(self.var_course.get(),))
                      con.commit()
                      messagebox.showinfo("Delete","Course deleted successfully",parent=self.root)
                      self.clear()
                  
        except Exception as ex:
                  messagebox.showerror("Error",f"Error due to{str(ex)}")
        
        





    def get_data(self,event):
        self.txt_CourseName.config(state='readonly')
        self.txt_CourseName
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        #print(row)
        self.var_course.set(row[1])
        self.var_Duration.set(row[2])
        self.var_Charges.set(row[3])
        #self.var_Desception.set(row[4])
        self.txt_Description.delete('1.0',END)
        self.txt_Description.insert(END,row[4])
                

    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
             messagebox.showerror("Error","Course Name should be Required",parent=self.root)
            else:
             cur.execute("select * from course where Name=?",(self.var_course.get(),))
             row=cur.fetchone()
             print(row)
             if row!=None:
                messagebox.showerror("Error","Course Name already present",parent=self.root)
             else:
                cur.execute("insert into course(Name,Duration,Charges,Description) values(?,?,?,?)",
                (
                self.var_course.get(),
                self.var_Duration.get(),
                self.var_Charges.get(),
                self.txt_Description.get("1.0",END)
              ))
                con.commit()
                messagebox.showinfo("success","Course Added Successfully",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")

    
    def Upadate(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
             messagebox.showerror("Error","Course Name should be Required",parent=self.root)
            else:
             cur.execute("select * from course where Name=?",(self.var_course.get(),))
             row=cur.fetchone()
             print(row)
             if row==None:
                messagebox.showerror("Error","Select course from list",parent=self.root)
             else:
                cur.execute("Update  course set ,Duration=?,Charges=?,Description=? Where Name=? ",
                (
                self.var_Duration.get(),
                self.var_Charges.get(),
                self.txt_Description.get("1.0",END),
                self.var_course.get(),
              ))
                con.commit()
                messagebox.showinfo("success","Course updated Successfully",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")



















            self.show()

    def show(self):
            con=sqlite3.connect(database="rms.db")
            cur=con.cursor()
            try:
                
                cur.execute("select * from course" )
                rows=cur.fetchall()
                self.CourseTable.delete(*self.CourseTable.get_children())
                for row in rows:
                    self.CourseTable.insert("",END,values=row)
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to{str(ex)}")
            

    def  search(self):
            con=sqlite3.connect(database="rms.db")
            cur=con.cursor()
            try:
                        
              cur.execute(f"select * from course where Name LIKE '%{self.var_Search.get()}%' " )
              rows=cur.fetchall()
              self.CourseTable.delete(*self.CourseTable.get_children())
              for row in rows:
                self.CourseTable.insert("",END,values=row)
            except Exception as ex:
                 messagebox.showerror("Error",f"Error due to{str(ex)}")
                    








if __name__ == "__main__":

     root = Tk()
     obj =CourseClass(root)
     root.mainloop()