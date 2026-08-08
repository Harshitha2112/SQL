from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class courseclass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student result Management System")
        self.root.geometry("1350x600+50+170")    # height and width
        self.root.config(bg="white")
        self.root.focus_force()

        #------title-------
        title=Label(self.root,text="Manage Course Details",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=1330,height=35)

        #-----------Variables---------
        self.var_cid=StringVar()
        self.var_course=StringVar()
        self.var_duration=StringVar()
        self.var_charges=StringVar()



        #---------widget---------
        lbl_courseid=Label(self.root,text="Course ID",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=60)

        lbl_courseName=Label(self.root,text="Course Name",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=100)
        lbl_duration=Label(self.root,text="Duration",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=140)
        lbl_charges=Label(self.root,text="Charges",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=180)
        lbl_description=Label(self.root,text="Description",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=220)
        # -------entry field----------
        self.txt_courseid = Entry(self.root, textvariable=self.var_cid, font=("goudy old style", 15, "bold"),
                                    bg="lightblue")
        self.txt_courseid.place(x=150, y=60, width=200)

        self.txt_courseName = Entry(self.root,textvariable=self.var_course, font=("goudy old style", 15, "bold"), bg="lightblue")
        self.txt_courseName.place(x=150, y=100,width=200)

        txt_duration = Entry(self.root,textvariable=self.var_duration, font=("goudy old style", 15, "bold"), bg="lightblue").place(x=150,  y=140,width=200)
        txt_charges = Entry(self.root,textvariable=self.var_charges, font=("goudy old style", 15, "bold"), bg="lightblue").place(x=150, y=180,width=200)

        self.txt_description = Text(self.root, font=("goudy old style", 15, "bold"), bg="lightblue")
        self.txt_description.place( x=150, y=220,width=500,height=130)


        #---------button-----------
        self.btn_add=Button(self.root,text="Save",font=("gaudy old style",15,"bold"),bg="green",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=150,y=400,width=110,height=40)

        self.btn_update = Button(self.root, text="Update", font=("gaudy old style", 15, "bold"), bg="green", fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=280, y=400, width=110, height=40)

        self.btn_delete = Button(self.root, text="Delete", font=("gaudy old style", 15, "bold"), bg="red", fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=410, y=400, width=110, height=40)

        self.btn_clear = Button(self.root, text="Clear", font=("gaudy old style", 15, "bold"), bg="grey", fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=540, y=400, width=110, height=40)



        #---------search---------
        self.var_search=StringVar()
        lbl_search_coursename=Label(self.root,text="Course Name",font=("goudy old style",15,'bold'),bg='white').place(x=720,y=60)
        txt_search_courseName = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15, "bold"),
                                    bg="lightblue")
        txt_search_courseName.place(x=870, y=60, width=300)
        btn_search = Button(self.root, text="Search", font=("gaudy old style", 15, "bold"), bg="#03a9f4", fg="white",
                              cursor="hand2",command=self.search)
        btn_search.place(x=1200, y=58, width=120, height=28)


        #--------content-----------
        self.c_frame=Frame(self.root,bd=2,relief=RIDGE)
        self.c_frame.place(x=720,y=100,width=600,height=470)                     #transparent box

        scrolly=Scrollbar(self.c_frame,orient=VERTICAL)
        scrollx=Scrollbar(self.c_frame,orient=HORIZONTAL)
        self.CourseTable=ttk.Treeview(self.c_frame,columns=("cid","name","duration","charges","description"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)






        self.CourseTable=ttk.Treeview(self.c_frame,columns=("cid","name","duration","charges","description"))
        self.CourseTable.heading("cid",text="Course ID")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("duration",text="Duration")
        self.CourseTable.heading("charges",text="Charges")
        self.CourseTable.heading("description",text="Description")
        self.CourseTable["show"]='headings'
        self.CourseTable.column("cid",width=50)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("duration",width=100)
        self.CourseTable.column("charges",width=100)
        self.CourseTable.column("description",width=100)

        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()



#----------------------------------------------------------------------
    def clear(self):
        self.show()
        self.var_cid.set("")
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.txt_description.delete('1.0', END)
        self.txt_description.config(state=NORMAL)

    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error", "Course Name should be required",
                                     parent=self.root)  # it shows error when course name is empty
            else:

                cur.execute("select * from c_table where name=?", (self.var_course.get(),))
                row = cur.fetchone()

                if row == None:
                    messagebox.showerror("Error", "please select course from the list first", parent=self.root)
                else:
                    op=messagebox.askyesno("confirm","do you really want to delete?",parent=self.root)
                    if op== True:
                        cur.execute("delete from c_table where name=?",(self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("delete","course deleted successfully",parent=self.root)
                        self.clear()

        except Exception as ex:
             messagebox.showerror("Error", f"Error due to {str(ex)}")


    def get_data(self,ev):
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
       # print(row)
        self.var_cid.set(row[0])
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        self.txt_description.delete('1.0',END)
        self.txt_description.insert(END,row[4])


#--------------update funtion-----------------

    def update(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course Name should be required",parent=self.root)            # it shows error when course name is empty
            else:

                cur.execute("select * from c_table where name=?", (self.var_course.get(),))
                row = cur.fetchone()

                if row== None:
                    messagebox.showerror("Error", " Select Course  From List", parent=self.root)
                else:
                    cur.execute("update c_table set  cid=?,duration=?,charges=?,description=? where name=?", (
                        self.var_cid.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0", END),
                        self.var_course.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Course update Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
             messagebox.showerror("Error", f"Error due to {str(ex)}")





    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course Name should be required",parent=self.root)            # it shows error when course name is empty
            else:

                cur.execute("select * from c_table where name=?", (self.var_course.get(),))
                row = cur.fetchone()

                if row!= None:
                    messagebox.showerror("Error", "Course Name already present", parent=self.root)
                else:
                    cur.execute("insert into c_table values(?,?,?,?,?)", (
                        self.var_cid.get(),
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0", END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Course Added Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
             messagebox.showerror("Error", f"Error due to {str(ex)}")


   #---------to display added course--------------

    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
                cur.execute("select * from c_table ")
                rows = cur.fetchall()
                self.CourseTable.delete(*self.CourseTable.get_children())
                for row in rows:
                    self.CourseTable.insert('',END,values=row)  # insert and display the data of course table

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute(f"select * from c_table where name LIKE '%{self.var_search.get()}%'")
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('', END, values=row)  # insert and display the data of course table

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

if __name__ == "__main__":
    root=Tk()
    obj=courseclass(root)
    root.mainloop()