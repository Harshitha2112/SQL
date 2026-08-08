from tkinter import *
from PIL import Image, ImageTk
from course import courseclass
from student import studentclass
from result import resultclass
from view import viewclass

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student result Management System")
        self.root.geometry("1600x900+0+0")    # height and width
        self.root.config(bg="white")         # background

        #icons
      #  self.logo_dash = ImageTk.PhotoImage(file="images/logo.png")

        # title
       # title=Label(self.root,text="Student Result Management System",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)

        title = Label(self.root,text="Student Result Management System",font=("goudy old style", 20, "bold"), bg="#033054", fg="white").place(x=0, y=0, relwidth=1, height=50)
        frame=LabelFrame(self.root,text="Menu",font=("times new roman",15),bg="white")
        frame.place(x=10,y=70,width=200,height=1340)

        course=Button(frame,text="Course",font=("goudy old style",15,"bold"),bg="purple",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=150,height=70)
        student=Button(frame,text="Student",font=("goudy old style",15,"bold"),bg="purple",fg="white",cursor="hand2",command=self.add_student).place(x=20,y=100,width=150,height=70)
        result=Button(frame,text="Result",font=("goudy old style",15,"bold"),bg="purple",fg="white",cursor="hand2",command=self.add_result).place(x=20,y=200,width=150,height=70)
        view=Button(frame,text="View",font=("goudy old style",15,"bold"),bg="purple",fg="white",cursor="hand2",command=self.add_view).place(x=20,y=300,width=150,height=70)


        self.bg_img=Image.open("images/bg.jpg")
        #self.bg_img=self.bg_img.resize(920,350),Image.ANTIALIAS
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        self.lbl_img=Label(self.root,image=self.bg_img).place(x=400,y=100,width=920,height=350)


        self.lbl_course=Label(self.root,text="Total Courses\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="red",fg="white").place(x=400,y=530,width=300,height=100)
        self.lbl_student=Label(self.root,text="Total Students\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="red",fg="white").place(x=710,y=530,width=300,height=100)
        self.lbl_result=Label(self.root,text="Total Results\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="red",fg="white").place(x=1020,y=530,width=300,height=100)



        #footer = Label(self.root,text="Student Result Management System \nContact us for any technical issues:99xxxxxx83",font=("goudy old style", 12), bg="black", fg="white").pack(side=BOTTOM,fill=X)

    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=courseclass(self.new_win)


    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=studentclass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = resultclass(self.new_win)


    def add_view(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = viewclass(self.new_win)





if __name__ == "__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()