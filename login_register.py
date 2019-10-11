from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox, ttk
import login_backend
#creating login page along with the register page.
class login:
     def __init__(self,window):

        self.window = window
        self.flag = 0

        self.frame = Frame(self.window,bg='Orange',width=700,height=400)  #creating frame

     def loginfn(self):

        self.label = Label(self.frame,text='Log In',bg='Orange',font=('Georgia',36,'bold'))

        self.name = Label(self.frame,text='Enter User_Name: ',bg='Orange',font=('Arial',18,'bold'))

        self.namee_text=StringVar()
        self.namee = Entry(self.frame,textvariable=self.namee_text,fg='gray',width=25,font=('Arial',16,'bold'))

        self.password1 = Label(self.frame,text='Enter Password : ',bg='Orange', fg='Green',font=('Arial',18,'bold'))

        self.password1e_text=StringVar()
        self.password1e = Entry(self.frame,textvariable=self.password1e_text,bg='White',fg='gray',width=25,font=('Arial',16,'bold'),show='*')

        self.buttonlogin = Button(self.frame,text='LOG IN',bg='gray',fg='gray12',font=('Georgia',18,'bold'),cursor='hand2', command=self.login_admin)


        if self.flag !=0:
            self.buttonAdmin = Button(self.frame,text='Admin',bg='Orange',fg='gray12',font=('Georgia',18,'bold'),cursor='hand2', command=self.adminbutton2)
        else:
            self.buttonAdmin = Button(self.frame,text='Admin',bg='Orange',fg='gray12',font=('Georgia',18,'bold'),cursor='hand2', command=self.adminbutton)

        self.buttonStudent = Button(self.frame,text='Student',bg='Orange',fg='gray12',font=('Georgia',18,'bold'),cursor='hand2', command=self.studentbutton)
	# placing

        self.label.place(x=40,y=40,width=200,height=80)

        self.name.place(x=100,y=140,width=240,height=60)

        self.namee.place(x=380,y=150,width=200,height=30)

        self.password1.place(x=85,y=220,width=240,height=30)

        self.password1e.place(x=380,y=215,width=200,height=30)

        self.buttonAdmin.place(x=320,y=30,width=140,height=50)

        self.buttonStudent.place(x=520,y=30,width=140,height=50)

        self.buttonlogin.place(x=180,y=300,width=140,height=50)

        self.frame.pack()


     def register(self):
         self.buttonAdmin.destroy()
         self.buttonStudent.destroy()
         self.label.destroy()
         self.name.destroy()
         self.namee.destroy()
         self.password1.destroy()
         self.password1e.destroy()
         self.buttonlogin.destroy()
         self.button2.destroy()

         self.labelr = Label(self.frame,text='Register',bg='Orange',font=('Georgia',32,'bold'))

         self.namer = Label(self.frame,text='Name : ',bg='Orange',font=('Arial',14,'bold'))

         self.namere_text=StringVar()
         self.namere = Entry(self.frame,textvariable=self.namere_text,fg='gray')

         self.idr = Label(self.frame,text='Roll No. : ',bg='Orange',font=('Arial',14,'bold'))

         self.rollno_text=StringVar()
         self.idre = Entry(self.frame,textvariable=self.rollno_text,fg='gray',width=25,font=('Arial',12,'bold'))

         self.passwordr1 = Label(self.frame,text='Create Password : ',bg='Orange', fg='Green',font=('Arial',14,'bold'))

         self.passwordr1e_text=StringVar()
         self.passwordr1e = Entry(self.frame,textvariable=self.passwordr1e_text,bg='White',fg='gray',width=25,font=('Arial',12,'bold'),show='*')

         self.passwordr2e_text=StringVar()
         self.passwordr2 = Label(self.frame,text='Reenter Password : ',bg='Orange', fg='Green',font=('Arial',14,'bold'))

         self.passwordr2e = Entry(self.frame,bg='White',fg='gray',width=25,font=('Arial',12,'bold'),show='*')

         self.buttonr = Button(self.frame,text='Register',bg='gray',fg='gray12',font=('Georgia',14,'bold'),cursor='hand2', command = self.create)

         self.buttonr2 = Button(self.frame,text='Back',bg='gray',fg='gray12',font=('Georgia',14,'bold'),cursor='hand2',  command= self.destroy)


         # placing
         self.labelr.place(x=40,y=10,width=200,height=80)

         self.namer.place(x=80,y=100,width=240,height=60)

         self.namere.place(x=300,y=115,width=200,height=30)

         self.idr.place(x=70,y=150,width=240,height=60)

         self.idre.place(x=300,y=165,width=200,height=30)

         self.passwordr1.place(x=28,y=210,width=240,height=30)

         self.passwordr1e.place(x=300,y=210,width=200,height=30)

         self.passwordr2.place(x=23,y=253,width=240,height=30)

         self.passwordr2e.place(x=300,y=253,width=200,height=30)

         self.buttonr.place(x=160,y=330,width=140,height=50)

         self.buttonr2.place(x=320,y=330,width=140,height=50)

     def create(self):
         if self.passwordr1e.get() != self.passwordr2e.get():
             messagebox.showinfo('error','Passwords do not match')
         elif len(self.namere.get()) == 0:
             messagebox.showinfo('error', 'Name field is empty')
         elif len(self.idre.get()) == 0:
            messagebox.showinfo('error', 'ID field is empty')
         elif len(self.passwordr1e.get()) == 0:
               messagebox.showinfo('error', 'PASSWORD field is empty')

         else:
             login_backend.insert(self.rollno_text.get(),self.namere_text.get(),self.passwordr1e_text.get())



     def adminbutton2(self):
        #z =button2.winfo_exists()
        #if z==1:
        self.button2.destroy()
        #messagebox.showinfo('<title>','<show>')
        self.name = Label(self.frame,text='Enter User_Name: ',bg='Orange',font=('Arial',18,'bold'))
        self.name.place(x=100,y=140,width=240,height=60)

     def adminbutton(self):
        self.name = Label(self.frame,text='Enter User_Name: ',bg='Orange',font=('Arial',18,'bold'))
        self.name.place(x=100,y=140,width=240,height=60)


     def studentbutton(self):
        self.flag =1
        self.buttonlogin.destroy()
        self.buttonlogin = Button(self.frame,text='LOG IN',bg='gray',fg='gray12',font=('Georgia',18,'bold'),cursor='hand2', command=self.login_student)
        self.buttonlogin.place(x=180,y=300,width=140,height=50)

        self.name = Label(self.frame,text='Enter Name: ',bg='Orange',font=('Arial',18,'bold'))
        self.name.place(x=100,y=140,width=240,height=60)
        self.button2 = Button(self.frame,text='SIGN UP',bg='gray',fg='gray12',font=('Georgia',18,'bold'),cursor='hand2', command=self.register)
        self.button2.place(x=340,y=300,width=140,height=50)

     def login_admin(self):
         if len(self.namee.get()) ==0:
                    messagebox.showinfo("ERROR", "Mendatory Field is empty")
         elif  len(self.password1e.get()) == 0:
                 messagebox.showinfo("ERROR", "Mendatory Field is empty")
         else:
             login_backend.check(self.namee_text.get(),self.password1e_text.get())

     def login_student(self):
          if len(self.namee.get()) ==0:
                     messagebox.showinfo("ERROR", "Mendatory Field is empty")
          elif  len(self.password1e.get()) == 0:
                  messagebox.showinfo("ERROR", "Mendatory Field is empty")
          else:
              login_backend.checks(self.namee_text.get(),self.password1e_text.get())

     def destroy(self):
         self.labelr.destroy()
         self.namer.destroy()
         self.namere.destroy()
         self.idr.destroy()
         self.idre.destroy()
         self.passwordr1.destroy()
         self.passwordr1e.destroy()
         self.passwordr2.destroy()
         self.passwordr2e.destroy()
         self.buttonr.destroy()
         self.buttonr2.destroy()
         self.buttonlogin.destroy()

         self.loginfn() # calling the loginfn function


# creating the window
window = Tk()
window.title('Login')
window.geometry('700x400')
# creating object to login class
obj = login(window)
obj.loginfn()
window.mainloop()
