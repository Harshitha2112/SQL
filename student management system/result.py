from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3
class resultclass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student result Management System")
        self.root.geometry("1350x600+50+170")    # height and width
        self.root.config(bg="white")
        self.root.focus_force()

        #------title-------
        title=Label(self.root,text="Add Student Results",font=("goudy old style",20,"bold"),bg="red",fg="white").place(x=10,y=15,width=1330,height=50)
#-----------------------variables-------------------

        self.var_roll=StringVar()

        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_marks_ob=StringVar()
        self.var_full_marks=StringVar()
        self.roll_list=[]
        self.fetch_roll()

#-----------------------widgets-------------

        lbl_select=Label(self.root,text="Select Student",font=("goudy old style",20,"bold"),bg="white").place(x=100,y=100)

        lbl_name=Label(self.root,text="Name",font=("goudy old style",20,"bold"),bg="white").place(x=100,y=160)
        lbl_course=Label(self.root,text="Course",font=("goudy old style",20,"bold"),bg="white").place(x=100,y=220)
        lbl_marks_ob=Label(self.root,text="Marks Obtained",font=("goudy old style",20,"bold"),bg="white").place(x=100,y=280)
        lbl_full_marks=Label(self.root,text="Full Marks",font=("goudy old style",20,"bold"),bg="white").place(x=100,y=340)

        self.txt_student = ttk.Combobox(self.root, textvariable=self.var_roll,
                                               values=(self.roll_list),
                                               font=("goudy old style", 20, "bold"), state="readonly", justify=CENTER)
        self.txt_student.place(x=350, y=100, width=250)
        self.txt_student.set("Select")

        btn_search = Button(self.root, text="Search", font=("gaudy old style", 20, "bold"), bg="#03a9f4", fg="white", cursor="hand2",command=self.search)
        btn_search.place(x=630, y=100, width=120, height=35)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 20, "bold"),  bg="lightblue",state="readonly")
        txt_name.place(x=350, y=160, width=300)

        txt_course = Entry(self.root, textvariable=self.var_course, font=("goudy old style", 20, "bold"),  bg="lightblue",state="readonly")
        txt_course.place(x=350, y=220, width=300)

        txt_marks_ob = Entry(self.root, textvariable=self.var_marks_ob, font=("goudy old style", 20, "bold"), bg="lightblue")
        txt_marks_ob.place(x=350, y=280, width=300)

        txt_full_marks = Entry(self.root, textvariable=self.var_full_marks, font=("goudy old style", 20, "bold"), bg="lightblue")
        txt_full_marks.place(x=350, y=340, width=300)


#-------------------buttons-------------------

        btn_add = Button(self.root, text="Add", font=("gaudy old style", 15, "bold"), bg="green", fg="white",  cursor="hand2",command=self.add)
        btn_add.place(x=350, y=450, width=120, height=35)

        btn_clear = Button(self.root, text="Clear", font=("gaudy old style", 15, "bold"), bg="grey", fg="white", cursor="hand2",command=self.clear)
        btn_clear.place(x=500, y=450, width=120, height=35)

#--------------------------------------------------

    def fetch_roll(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select roll from Student ")
            rows = cur.fetchall()
            v=[]
            if len(rows)>0:
                for row in rows:
                    self.roll_list.append(row[0])
           # print(v)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")



    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select name,course from Student where roll=?", (self.var_roll.get(),))
            row = cur.fetchone()
            if row != None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])

            else:
                messagebox.showerror("Error", "no record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", "NO record found", parent=self.root)



    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","please search student record",parent=self.root)            # it shows error when course name is empty
            else:

                cur.execute("select * from result where roll=? and course=?",(self.var_roll.get(), self.var_course.get()))
                row = cur.fetchone()

                if row!= None:
                    messagebox.showerror("Error", "Result already present", parent=self.root)
                else:
                    per=(int(self.var_marks_ob.get())*100)/int(self.var_full_marks.get())
                    cur.execute("insert into result(roll,name,course,marks_ob,full_marks,per) values(?,?,?,?,?,?)", (
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_marks_ob.get(),
                        self.var_full_marks.get(),
                        str(per)
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Course Added Successfully", parent=self.root)

        except Exception as ex:
             messagebox.showerror("Error", f"Error due to {str(ex)}")




    def clear(self):
        self.var_roll.set("Select"),
        self.var_name.set(""),
        self.var_course.set(""),
        self.var_marks_ob.set(""),
        self.var_full_marks.set("")




if __name__ == "__main__":
    root=Tk()
    obj=resultclass(root)
    root.mainloop()