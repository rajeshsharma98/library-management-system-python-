from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox, ttk
#creating login page

class login:
     def __init__(self,window):

        self.window = window

        self.frame = Frame(self.window,bg='Orange',width=700,height=400)  #creating frame

        self.label = Label(self.frame,text='Log In',bg='Orange',font=('Georgia',36,'bold'))

        self.name = Label(self.frame,text='Enter Roll NO: ',bg='Orange',font=('Arial',18,'bold'))

        self.namee = Entry(self.frame,fg='gray',width=25,font=('Arial',16,'bold'))

        self.password1 = Label(self.frame,text='Enter Password : ',bg='Orange', fg='Green',font=('Arial',18,'bold'))

        self.password1e = Entry(self.frame,bg='White',fg='gray',width=25,font=('Arial',16,'bold'),show='*')

        self.button = Button(self.frame,text='LOG IN',bg='gray',fg='gray12',font=('Georgia',18,'bold'),cursor='hand2')

        self.button2 = Button(self.frame,text='Register',bg='gray',fg='gray12',font=('Georgia',18,'bold'),cursor='hand2')


		# placing

        self.label.place(x=40,y=40,width=200,height=80)

        self.name.place(x=100,y=140,width=240,height=60)

        self.namee.place(x=380,y=150,width=200,height=30)

        self.password1.place(x=85,y=220,width=240,height=30)

        self.password1e.place(x=380,y=215,width=200,height=30)

        self.button.place(x=180,y=300,width=140,height=50)

        self.button2.place(x=340,y=300,width=140,height=50)

        self.frame.pack()


# creating the window
window = Tk()
window.title('Login')
window.geometry('700x400')

# creating object to login class
obj = login(window)

window.mainloop()
