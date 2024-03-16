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







root.mainloop()











