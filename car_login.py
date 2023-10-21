from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import pymongo, os
#import credentials as cr
#from signup_page import SignUp


class Blood:
    def __init__(self, root):
        self.window = root
        self.window.title("Sign Up")
        self.window.geometry("1280x800+0+0")
        self.window.config(bg = "red")

        self.bg_img = ImageTk.PhotoImage(file="s-class.jpg")
        background = Label(self.window,image=self.bg_img).place(x=-300,y=0,relwidth=1,relheight=1)
        frame = Frame(self.window, bg="white")
        frame.place(x=700,y=100,width=500,height=600)

        title1 = Label(frame, text="Modern Bloodbank", font=("times new roman",25,"bold"),bg="white", fg="red").place(x=20, y=10)
        title2 = Label(frame, text="Join with us", font=("times new roman",13),bg="white", fg="black").place(x=20, y=50)

        fname = Label(frame, text="First name", font=("helvetica",15,"bold"),bg="white").place(x=20, y=100)
        lname = Label(frame, text="Last name", font=("helvetica",15,"bold"),bg="white").place(x=240, y=100)

        self.fname_txt = Entry(frame,font=("arial"))
        self.fname_txt.place(x=20, y=130, width=200)

        self.lname_txt = Entry(frame,font=("arial"))
        self.lname_txt.place(x=240, y=130, width=200)

        cont = Label(frame, text="Contact Number", font=("helvetica", 15, "bold"), bg="white").place(x=20, y=180)

        self.cont_txt = Entry(frame, font=("arial"))
        self.cont_txt.place(x=20, y=210, width=420)

        email = Label(frame, text="Email", font=("helvetica",15,"bold"),bg="white").place(x=20, y=240)

        self.email_txt = Entry(frame,font=("arial"))
        self.email_txt.place(x=20, y=280, width=420)

        sec_question = Label(frame, text="Blood type", font=("helvetica",15,"bold"),bg="white").place(x=20, y=310)
        answer = Label(frame, text="Positive or negative", font=("helvetica",15,"bold"),bg="white").place(x=240, y=310)

        self.questions = ttk.Combobox(frame,font=("helvetica",13),state='readonly',justify=CENTER)
        self.questions['values'] = ("Select","A","B","AB", "O")
        self.questions.place(x=20,y=340,width=200)
        self.questions.current(0)

        # self.questions = ttk.Combobox(frame, font=("helvetica", 13), state='readonly', justify=CENTER)
        # self.questions['values'] = ("Select","+","-")
        # self.questions.place(x=240, y=290, width=200)
        # self.questions.current(0)

        self.answer_txt = Entry(frame,font=("arial"))
        self.answer_txt.place(x=240, y=340, width=200)

        password =  Label(frame, text="Doctor Assigned", font=("helvetica",15,"bold"),bg="white").place(x=20, y=370)

        self.password_txt = Entry(frame,font=("arial"))
        self.password_txt.place(x=20, y=400, width=420)

        self.terms = IntVar()
        terms_and_con = Checkbutton(frame,text="I Agree The Terms & Conditions",variable=self.terms,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=20,y=450)
        self.signup = Button(frame,text="Sign Up",command=self.signup_func,font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="green2",fg="white").place(x=120,y=500,width=250)

    def signup_func(self):
        if self.fname_txt.get()=="" or self.lname_txt.get()=="" or self.cont_txt.get()=="" or self.email_txt.get()=="" or self.questions.get()=="Select" or self.answer_txt.get()=="" or self.password_txt.get() == "":
            messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.window)

        elif self.terms.get() == 0:
            messagebox.showerror("Error!","Please Agree with our Terms & Conditions",parent=self.window)

        else:
                client=pymongo.MongoClient('mongodb://localhost:27017')
                mydb=client['adbms']
                information = mydb.table1
                rec= [{"First Name":self.fname_txt.get(),
                       "Last Name":self.lname_txt.get(),
                       "Contact Number":self.cont_txt.get(),
                       "Email  Address":self.email_txt.get(),
                       "Blood Type":self.questions.get(),
                       "Positive or Negative":self.answer_txt.get(),
                       "Doctor Assigned":self.password_txt.get()}]
               # self.fname_txt.get(),
                #self.lname_txt.get(),
              #  self.cont_txt.get(),
                #  self.email_txt.get(),
                # self.questions.get(),
                # self.answer_txt.get(),
                #self.password_txt.get()
                uid = information.insert_many(rec)
                print(uid)
    def reset_fields(self):
        self.fname_txt.delete(0, END)
        self.lname_txt.delete(0, END)
        self.cont_txt.delete(0, END)
        self.email_txt.delete(0, END)
        self.questions.current(0)
        self.answer_txt.delete(0, END)
        self.password_txt.delete(0, END)

if __name__ == "__main__":
    root = Tk()
   # obj = SignUp(root)
    obj = Blood(root)
    root.mainloop()