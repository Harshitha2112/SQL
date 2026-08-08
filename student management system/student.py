from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class studentclass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student result Management System")
        self.root.geometry("1350x600+50+170")    # height and width
        self.root.config(bg="white")
        self.root.focus_force()

        #------title-------
        title=Label(self.root,text="Manage Student Details",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=1330,height=35)

        #-----------Variables---------

        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_contact=StringVar()
        self.var_course=StringVar()
        self.var_state=StringVar()
        self.var_city=StringVar()
        self.var_admission=StringVar()
        self.var_address=StringVar()







        #---------widget [column 1]---------
        lbl_roll=Label(self.root,text="Roll No.",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=60)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=100)
        lbl_Email=Label(self.root,text="Email",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=140)
        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=180)
        lbl_state=Label(self.root,text="State",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=220)

        txt_state = Entry(self.root, textvariable=self.var_state, font=("goudy old style", 15, "bold"),
                        bg="lightblue")
        txt_state.place(x=150, y=220, width=200)

        lbl_city = Label(self.root, text="City", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=220)

        txt_city = Entry(self.root, textvariable=self.var_city, font=("goudy old style", 15, "bold"),
                          bg="lightblue")
        txt_city.place(x=480, y=220, width=200)


        lbl_address=Label(self.root,text="Address",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=260)


        # -------entry field  1----------


        self.txt_roll = Entry(self.root, textvariable=self.var_roll, font=("goudy old style", 15, "bold"), bg="lightblue")
        self.txt_roll.place(x=150, y=60, width=200)

        txt_name = Entry(self.root,textvariable=self.var_name, font=("goudy old style", 15, "bold"), bg="lightblue").place(x=150,  y=100,width=200)
        txt_email = Entry(self.root,textvariable=self.var_email, font=("goudy old style", 15, "bold"), bg="lightblue").place(x=150, y=140,width=200)
        self.txt_gender = ttk.Combobox(self.root,textvariable=self.var_gender,values=("select","male","female","other") ,font=("goudy old style", 15, "bold"), state="readonly",justify=CENTER)
        self.txt_gender.place(x=150, y=180,width=200)
        self.txt_gender.current(0)

        self.txt_address = Text(self.root, font=("goudy old style", 15, "bold"), bg="lightblue")
        self.txt_address.place( x=150, y=260,width=540,height=100)




    #-----------widget[column 2]--------------------
        lbl_dob = Label(self.root, text="D.O.B", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=60)
        lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=100)
        lbl_admission = Label(self.root, text="Admission", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=140)
        lbl_course = Label(self.root, text="Course", font=("goudy old style", 15, "bold"), bg="white").place(x=360,
                                                                                                             y=180)

        # -------entry field   2----------


        self.course_list=[]
        self.fetch_course()
        txt_dob= Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 15, "bold"),
                              bg="lightblue")
        txt_dob.place(x=480, y=60, width=200)

        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15, "bold"),
                         bg="lightblue").place(x=480, y=100, width=200)
        txt_admission = Entry(self.root, textvariable=self.var_admission, font=("goudy old style", 15, "bold"),
                          bg="lightblue").place(x=480, y=140, width=200)
        self.txt_course = ttk.Combobox(self.root, textvariable=self.var_course,
                                       values=(self.course_list),
                                       font=("goudy old style", 15, "bold"), state="readonly", justify=CENTER)
        self.txt_course.place(x=480, y=180, width=200)
        self.txt_course.set("Select")


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
        lbl_search_roll=Label(self.root,text="Roll No.",font=("goudy old style",15,'bold'),bg='white').place(x=720,y=60)
        txt_search_roll = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15, "bold"),
                                    bg="lightblue")
        txt_search_roll.place(x=870, y=60, width=300)
        btn_search = Button(self.root, text="Search", font=("gaudy old style", 15, "bold"), bg="#03a9f4", fg="white",
                              cursor="hand2",command=self.search)
        btn_search.place(x=1200, y=58, width=120, height=28)


        #--------content-----------
        self.c_frame=Frame(self.root,bd=2,relief=RIDGE)
        self.c_frame.place(x=720,y=100,width=600,height=470)                     #transparent box

        scrolly=Scrollbar(self.c_frame,orient=VERTICAL)
        scrollx=Scrollbar(self.c_frame,orient=HORIZONTAL)
        self.CourseTable=ttk.Treeview(self.c_frame,columns=("roll","name","email","gender","dob","contact","admission","course","state","city","address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)






        self.CourseTable=ttk.Treeview(self.c_frame,columns=("roll","name","email","gender","dob","contact","admission","course","state","city","city","address"))
        self.CourseTable.heading("roll",text="Roll No.")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("email",text="Email")
        self.CourseTable.heading("gender",text="Gender")
        self.CourseTable.heading("dob",text="D.O.B")
        self.CourseTable.heading("contact",text="Contact")
        self.CourseTable.heading("admission",text="Admission")
        self.CourseTable.heading("course",text="Course")
        self.CourseTable.heading("state",text="State")
        self.CourseTable.heading("city",text="City")
        self.CourseTable.heading("address",text="Address")


        self.CourseTable["show"]='headings'
        self.CourseTable.column("roll",width=50)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("email",width=100)
        self.CourseTable.column("gender",width=100)
        self.CourseTable.column("dob",width=100)
        self.CourseTable.column("contact",width=100)
        self.CourseTable.column("admission",width=100)
        self.CourseTable.column("course",width=100)
        self.CourseTable.column("state",width=100)
        self.CourseTable.column("city",width=100)
        self.CourseTable.column("address",width=200)

        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()



#----------------------------------------------------------------------
    def clear(self):
        self.show()

        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_admission.set("")
        self.var_course.set("")
        self.var_state.set("")
        self.var_city.set("")
        self.txt_address.delete("1.0", END)
        self.txt_roll.config(state=NORMAL)
        self.var_search.set("")

    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll No. should be required",
                                     parent=self.root)  # it shows error when course name is empty
            else:

                cur.execute("select * from Student where roll=?", (self.var_roll.get(),))
                row = cur.fetchone()

                if row == None:
                    messagebox.showerror("Error", "please select student from the list first", parent=self.root)
                else:
                    op=messagebox.askyesno("confirm","do you really want to delete?",parent=self.root)
                    if op== True:
                        cur.execute("delete from Student where roll=?",(self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("delete","student deleted successfully",parent=self.root)
                        self.clear()

        except Exception as ex:
             messagebox.showerror("Error", f"Error due to {str(ex)}")



#-------------to display data when you click on a particular row-------------------


    def get_data(self,ev):
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
       # print(row)
        self.var_roll.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_dob.set(row[4]),
        self.var_contact.set(row[5]),
        self.var_admission.set(row[6]),
        self.var_course.set(row[7]),
        self.var_state.set(row[8]),
        self.var_city.set(row[9]),
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[10])



#--------------update funtion-----------------

    def update(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll No. should be required",parent=self.root)            # it shows error when course name is empty
            else:

                cur.execute("select * from Student where roll=?", (self.var_roll.get(),))
                row = cur.fetchone()

                if row== None:
                    messagebox.showerror("Error", " Select Student  From List", parent=self.root)
                else:
                    cur.execute("update Student set name=?,email=?,gender=?,dob=?,contact=?,admission=?,course=?,state=?,city=?,address=? where roll=?", (

                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_admission.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.txt_address.get("1.0",END),
                        self.var_roll.get()

                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Student update Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
             messagebox.showerror("Error", f"Error due to {str(ex)}")





    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll number should be required",parent=self.root)            # it shows error when course name is empty
            else:

                cur.execute("select * from Student where roll=?", (self.var_roll.get(),))
                row = cur.fetchone()

                if row!= None:
                    messagebox.showerror("Error", "Roll number already present", parent=self.root)
                else:
                    cur.execute("insert into Student(roll,name,email,gender,dob,contact,admission,course,state,city,address) values(?,?,?,?,?,?,?,?,?,?,?)", (

                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_admission.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_address.get()

                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Student Added Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
             messagebox.showerror("Error", f"Error due to {str(ex)}")


   #---------to display added course--------------

    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
                cur.execute("select * from Student ")
                rows = cur.fetchall()
                self.CourseTable.delete(*self.CourseTable.get_children())
                for row in rows:
                    self.CourseTable.insert('',END,values=row)  # insert and display the data of course table

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def fetch_course(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select name from c_table ")
            rows = cur.fetchall()
            v=[]
            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])
           # print(v)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    #-----------------search course by their name-------------------------
    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from Student where roll=?", (self.var_search.get(),))
            row= cur.fetchone()
            if row!=None:
                 self.CourseTable.delete(*self.CourseTable.get_children())
                 self.CourseTable.insert('', END, values=row)  # insert and display the data of course table
            else:
                messagebox.showerror("Error","no record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", "NO record found",parent=self.root)

if __name__ == "__main__":
    root=Tk()
    obj=studentclass(root)
    root.mainloop()