from tkinter import *
from datetime import date
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from tkinter.ttk import Combobox
import openpyxl, xlrd
from openpyxl import Workbook
import pathlib



background = "#06283D"
framebg="#EDEDED"
framefg="#06283D"

root = Tk()
root.title("Student Registration System")
root.geometry("1200x600+50+50")
root.config(bg=background)

#Creating data saving file in excel

file = pathlib.Path('Student_data.xlsx')
if file.exists():
    pass
else:
    file=Workbook()
    sheet = file.active
    sheet['A1']="Registration No."
    sheet['B1']="Name"
    sheet['C1']="Class"
    sheet['D1']="Gender"
    sheet['E1']="DOB"
    sheet['F1']="Date of registration"
    sheet['G1']="Religion"
    sheet['H1']="Skills"
    sheet['I1']="Father's Name"
    sheet['J1']="Mother's Name"
    sheet['K1']="Father's Occupation"
    sheet['L1']="Mother's Occupation"

    file.save('Student_data.xlsx')

#gender

def selection():
    value=radio.get()
    if value ==1:
        gender="Male"
        print(gender)
    else:
        gender="Female"
        print(gender)



#top frames
Label(root,text="Email:ijse@gmail.com",width=8,height=2,bg="#f0687c",anchor='e').pack(side=TOP,fill=X)
Label(root,text="STUDENT REGISTRATION",width=8,height=2,bg="#c36464",fg='#fff',font='arial 15 bold').pack(side=TOP,fill=X)

#search box to update
Search = StringVar()
Entry(root,textvariable=Search,width=20,bd=2,font='arial 16').place(x=800,y=50)
imageicon3=PhotoImage(file="images/search.png")
srch=Button(root,text="Search",compound=LEFT,width=100,image=imageicon3,bg='#68ddfa',font='arial 10 bold')
srch.place(x=1060,y=51)

imageicon4= PhotoImage(file="images/layers.png")
Update_button=Button(root,image=imageicon4,bg="#c36464")
Update_button.place(x=90,y=47)


#Registration and date
Label(root,text="Registration No:",font='arial 10',fg=framebg,bg=background).place(x=28,y=120)
Label(root,text="Date:",font='arial 10',fg=framebg,bg=background).place(x=490,y=120)

Registration=StringVar()
Date = StringVar()
reg_entry = Entry(root,textvariable=Registration,width=15,font='arial 12')
reg_entry.place(x=145,y=120)

#Registration date()

today=date.today()
d1= today.strftime("%d/%m/%y")
date_entry = Entry(root,textvariable=Date,width=15,font='arial 12')
date_entry.place(x=540,y=120)
Date.set(d1)

#Student detail

obj=LabelFrame(root,text="Student's Deatil",font=18,bd=2,width=880,bg=framebg,fg=framefg,height=210,relief=GROOVE)
obj.place(x=20,y=170)

Label(obj,text="Full name:",font='arial 12',bg=framebg,fg=framefg).place(x=20,y=35)
Label(obj,text="Date of Birth:",font='arial 12',bg=framebg,fg=framefg).place(x=20,y=85)
Label(obj,text="Gender:",font='arial 12',bg=framebg,fg=framefg).place(x=20,y=135)

Label(obj,text="Class:",font='arial 12',bg=framebg,fg=framefg).place(x=480,y=35)
Label(obj,text="Religon:",font='arial 12',bg=framebg,fg=framefg).place(x=480,y=85)
Label(obj,text="Skills:",font='arial 12',bg=framebg,fg=framefg).place(x=480,y=135)

Name = StringVar()
name_entry = Entry(obj,textvariable=Name,width=20,font='arial 8')
name_entry.place(x=140,y=35)

DOB = StringVar()
dob_entry = Entry(obj,textvariable=DOB,width=20,font='arial 8')
dob_entry.place(x=140,y=85)

radio = IntVar()
R1= Radiobutton(obj,text="Male",variable=radio,value=1,bg=framebg,fg=framefg,command=selection)
R1.place(x=130,y=135)
R2= Radiobutton(obj,text="Female",variable=radio,value=2,bg=framebg,fg=framefg,command=selection)
R2.place(x=200,y=135)



#Parents detail

obj=LabelFrame(root,text="Parents' Deatil",font=18,bd=2,width=880,bg=framebg,fg=framefg,height=180,relief=GROOVE)
obj.place(x=20,y=390)



root.mainloop()











