#!/usr/bin/python 
#################################### 
#    Name : Mwende
#    Date :02/ 06/ 2022 
##################################### 

from tkinter import *

window = Tk()
window.title("Welcome to my App")
window.configure(bg = 'yellow')
window.geometry("700 x 600")

f_name=Label( window ,text="first name",font=("Arial",36))
f_name=Label( window ,text="second name",font=("Arial",36))

f.name.grid(column=60,row=100)
s.name.grid(column=60,row=120)

def open_popup():
    top = Toplevel(window)
    top.geometry("300 x 300")
    top.title("Pop Up Window")
    top.configure(bg = 'green')
    msg =Label(top, text = "Welcome to the pop up")

btn=Button(window , text="Click me" , bg='black', fg='red', command = open)
btn.grid(column = 120, row = 150) 

f_name_box = Entry(window , width = 20)
f_name_box.grid(column = 100,row=100)

s_name_box = Entry(window , width = 20)
s_name_box.grid(column = 100,row=120)