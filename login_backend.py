import sqlite3
from tkinter import *
from admin import admin
from student import student

def connect():
    conn=sqlite3.connect("login.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE if NOT exists user(roll no INTEGER PRIMARY KEY,name text,password text)")
    #cur.execute("drop table user")
    # create table 'admin' add some entries in it, by applying same procedure done to add some entries in user table,
    # before that replace user by admin in the 'insert' function . After adding up the entries roll back the changes.
    conn.commit()
    conn.close()

def insert(rollno,name,password):
    conn=sqlite3.connect('login.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO user VALUES(?,?,?)',(rollno,name,password))
    conn.commit()
    conn.close()

def check(name,password):
    conn=sqlite3.connect('login.db')
    cur = conn.cursor()
    if   (cur.execute('SELECT * FROM admin WHERE name =? AND password = ?',(name,password))):
        if cur.fetchone():
            window = Tk()
            window.title('Admin_User')
            window.geometry('700x450')
            obj=admin(window)
            window.mainloop()
        else:
            messagebox.showinfo('error','INVALID CREDENTIALS for ADMIN LOGIN')

def checks(name,password):                       # for student login
    conn=sqlite3.connect('login.db')
    cur = conn.cursor()
    if   (cur.execute('SELECT * FROM user WHERE name = ? AND password = ?', (name, password))):
        if cur.fetchone():
            window = Tk()
            window.title('Student_User')
            window.geometry('700x400')
            obj = student(window)
            window.mainloop()
        else:
            messagebox.showinfo('error','INVALID CREDENTIALS for STUDENT LOGIN')


    conn.commit()
    conn.close()

connect()
