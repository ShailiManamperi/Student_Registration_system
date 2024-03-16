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



root.mainloop()











