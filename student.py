from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk


from tkinter import *
import backend

class student:
        def __init__(self,window):
            self.window = window

            self.frame = Frame(self.window, bg = 'orange', width=700,height=400)

            self.frame.pack()

            self.label = Label(self.frame,text='Student User',bg='Orange',font=('Georgia',30,'bold'))
            self.label.place(x=20,y=20,width=400,height=50)

            self.label_title = Label(self.frame, text='TITLE',bg='orange',font=('Georgia',14,'bold'))
            self.label_title.place(x=20,y=100,width=100,height=50)

            self.label_year = Label(self.frame, text='YEAR',bg='orange',font=('Georgia',14,'bold'))
            self.label_year.place(x=20,y=150,width=100,height=30)


            self.label_author = Label(self.frame, text='AUTHOR',bg='orange',font=('Georgia',14,'bold'))
            self.label_author.place(x=350,y=100,width=100,height=30)

            self.label_isbn = Label(self.frame, text='ISBN',bg='orange',font=('Georgia',14,'bold'))
            self.label_isbn.place(x=350,y=150,width=100,height=30)

            self.title_text=StringVar()
            self.entry_title = Entry(self.frame, fg='gray',textvariable=self.title_text,width=25,font=('Arial',12,'bold'))
            self.entry_title.place(x=120,y=100,width=150,height=30)

            self.year_text=StringVar()
            self.entry_year = Entry(self.frame, fg='gray',textvariable=self.year_text,width=25,font=('Arial',12,'bold'))
            self.entry_year.place(x=120,y=150,width=150,height=30)


            self.author_text=StringVar()
            self.entry_author = Entry(self.frame, fg='gray',textvariable=self.author_text,width=25,font=('Arial',12,'bold'))
            self.entry_author.place(x=470,y=100,width=150,height=30)

            self.isbn_text=StringVar()
            self.entry_isbn = Entry(self.frame, fg='gray',textvariable=self.isbn_text,width=25,font=('Arial',12,'bold'))
            self.entry_isbn.place(x=470,y=150,width=150,height=30)


            self.listbox = Listbox(self.frame)
            self.listbox.place(x=100,y=200,width=500,height=100)

       #    sb1=Scrollbar(window)
        #    sb1.grid(row=3,column=2,rowspan=6)

        #    list1.configure(yscrollcommand=sb1.set)
        #    sb1.configure(command=list1.yview)
        #    self.listbox.bind("<<ListboxSelect>>",get_selected_row())

            self.button_view = Button(self.frame,text='View All', command=self.view_command)
            self.button_view.place(x=100,y=320,width=100,height=40)

            self.button_search = Button(self.frame,text='Search ', command=self.search_command)
            self.button_search.place(x=200,y=320,width=100,height=40)

            self.button_issue = Button(self.frame,text='Issue', command=self.issue_command)
            self.button_issue.place(x=300,y=320,width=100,height=40)

            self.button_request = Button(self.frame, text='Request', command = self.request_command)
            self.button_request.place(x=400, y=320,width=100,height=40)

            self.button_issue = Button(self.frame, text='Clear Fields', command=self.clear_command)
            self.button_issue.place(x=500, y=320,width=100,height=40)
            #b6=Button(window,text="CLOSE WINDOW",width=14,command=window.destroy)
            #b6.grid(row=8,column=3)

        def clear_command(self):
            self.entry_title.delete(0,END)
            self.entry_year.delete(0,END)
            self.entry_author.delete(0,END)
            self.entry_isbn.delete(0,END)

        def request_command(self):
            backend.request_insert(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())
            self.listbox.delete(0,END)
            self.listbox.insert(END,(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get()))



        def issue_command(self):
            selected_tuple=self.listbox.curselection()
            value = self.listbox.get(selected_tuple)
            self.entry_title.delete(0,END)
            self.entry_title.insert(END,value[1])
            self.entry_year.delete(0,END)
            self.entry_year.insert(END,value[2])
            self.entry_author.delete(0,END)
            self.entry_author.insert(END,value[3])
            self.entry_isbn.delete(0,END)
            self.entry_isbn.insert(END,value[4])
            backend.issue_insert(value[0])

        def view_command(self):
            self.listbox.delete(0,END) # it will empty the list every time it is called
            for row in backend.view():
                self.listbox.insert(END,row) # END ensures that every new entry is stored at end of the all rows

        def search_command(self):
            self.listbox.delete(0,END) # gives an empty list
            for row in backend.search(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get()):
                self.listbox.insert(END,row)


        def add_command(self):
            backend.insert(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())
            self.listbox.delete(0,END)
            self.listbox.insert(END,(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get()))


        def delete_command(self):
            selected_tuple=self.listbox.curselection()
            value = self.listbox.get(selected_tuple)
            self.entry_title.delete(0,END)
            self.entry_title.insert(END,value[1])
            self.entry_year.delete(0,END)
            self.entry_year.insert(END,value[2])
            self.entry_author.delete(0,END)
            self.entry_author.insert(END,value[3])
            self.entry_isbn.delete(0,END)
            self.entry_isbn.insert(END,value[4])

            backend.delete(value[0])
            # whether i havae to use [0] here or at backend

        def update_command(self):
            selected_tuple=self.listbox.curselection()
            value = self.listbox.get(selected_tuple)
            self.entry_title.delete(0,END)
            self.entry_title.insert(END,value[0])
            self.entry_year.delete(0,END)
            self.entry_year.insert(END,value[1])
            self.entry_author.delete(0,END)
            self.entry_author.insert(END,value[2])
            self.entry_isbn.delete(0,END)
            self.entry_isbn.insert(END,value[3])
            backend.update(value[0],self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())




window = Tk()
window.title('Student User')
window.geometry('700x400')
obj = student(window)
window.mainloop()



'''
class student:
    def __init__(self,window):

        self.window = window

        self.frame = Frame(self.window, bg = 'orange', width=700,height=400)

        self.label_heading = Label(self.frame, text='Student Login', bg='Orange',fg='black',font=('Arial',18,'bold'))
        self.label_heading.place(x=100, y=0, width=400,height=40)

        self.frame.pack()

        self.title = Label(self.frame,text='Enter title of the book:', bg='Orange',font=('Arial',18,'bold'))

        self.titlee = Entry(self.frame, fg='gray', width=25,font=('Arial',16,'bold'))

        self.author = Label(self.frame, text='Enter name of the Author:', bg='Orange',font=('Arial',18,'bold'))

        self.authore = Entry(self.frame, fg='gray',font=('Arial',16,'bold'))

        self.button_search = Button(self.frame, text='Search', bg='gray', fg='gray12',font=('Georgia',18,'bold'),cursor='hand2')
        self.button_request = Button(self.frame, text='Request', bg='gray', fg='gray12',font=('Georgia',18,'bold'),cursor='hand2')

        #placing

        self.title.place(x=100,y=135,width=260,height=60)
        self.titlee.place(x=420,y=150,width=240,height=30)
        self.author.place(x=85,y=220,width=300,height=30)
        self.authore.place(x=420,y=215,width=240,height=30)
        self.button_search.place(x=200, y=330,width=140,height=50)
        self.button_request.place(x=350, y=330,width=140,height=50)

    def request_book(self):
        self.title.destroy()
        self.titlee.destroy()
        self.author.destroy()
        self.authore.destroy()
        self.button.destroy()

        self.rtitle = Label(self.frame,text='Enter title of the book:', bg='Orange',font=('Arial',18,'bold'))

        self.rtitlee = Entry(self.frame, fg='gray', width=25,font=('Arial',16,'bold'))

        self.rauthor = Label(self.frame, text='Enter name of the Author:', bg='Orange',font=('Arial',18,'bold'))

        self.rauthore = Entry(self.frame, fg='gray',font=('Arial',16,'bold'))

        self.rid = Label(self.frame, text='Enter your ID:', bg='Orange',font=('Arial',18,'bold'))

        self.ride = Entry(self.frame, fg='gray',font=('Arial',16,'bold'))

        self.rbutton = Button(self.frame, text='Request', bg='gray', fg='gray12',font=('Georgia',18,'bold'),cursor='hand2')

        #placing

        self.rtitle.place(x=100,y=150,width=260,height=30)
        self.rtitlee.place(x=420,y=150,width=240,height=30)

        self.rauthor.place(x=85,y=220,width=300,height=30)
        self.rauthore.place(x=420,y=215,width=240,height=30)



        self.rbutton.place(x=250, y=330,width=140,height=50)
    def destroy(self):
        self.title.destroy()
        self.titlee.destroy()
        self.author.destroy()
        self.authore.destroy()
        self.button.destroy()

        self.search_book()


window = Tk()
window.title('Student')
window.geometry('700x400')
obj = student(window)

window.mainloop()
'''
