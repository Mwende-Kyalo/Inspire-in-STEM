#!/usr/bin/python 
#################################### 
#    Name : Mwende
#    Date :02/ 06/ 2022 
##################################### 

from tkinter import *

window = Tk()
window.title("Welcome to my App")
window.configure(bg = 'light blue')
#window.geometry("700 x 400")

u_name=Label( window ,text="User name",font=("Arial",20))
f_name=Label( window ,text="First name",font=("Arial",20))
s_name=Label( window ,text="Second name",font=("Arial",20))
p_name=Label( window ,text="Type password",font=("Arial",20))
pw_name=Label( window ,text="Confirm password",font=("Arial",20))

u_name.grid(column=160,row=200)
f_name.grid(column=160,row=120)
s_name.grid(column=160,row=140)
p_name.grid(column=160,row=160)
pw_name.grid(column=160,row=180)

def open_popup():
    top = Toplevel(window)
    top.geometry("300 x 300")
    top.title("Pop Up Window")
    top.configure(bg = 'green')
    msg =Label(top, text = "Welcome to the pop up")

btn=Button(window , text="Log in " , bg='black', fg='red', command = open)
btn.grid(column = 240, row = 150) 

btn=Button(window , text="Set up account " , bg='black', fg='red', command = open)
btn.grid(column = 240, row = 150) 

u_name_box = Entry(window , width = 20)
u_name_box.grid(column = 200,row=100)

f_name_box = Entry(window , width = 20)
f_name_box.grid(column = 200,row=120)

s_name_box = Entry(window , width = 20)
s_name_box.grid(column = 200,row=140)

p_name_box = Entry(window , width = 20)
p_name_box.grid(column = 200,row=160)

pw_name_box = Entry(window , width = 20)
pw_name_box.grid(column = 200,row=180)

window.mainloop()