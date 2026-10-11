from tkinter import *
from tkinter.ttk import *

win = Tk()

def Add():
    global Num2Ent
    global Num1Ent
    AddResult = int(Num1Ent.get()) + int(Num2Ent.get())
    Reslbl.config(text="Result: "+str(AddResult))

def Subtract():
    global Num2Ent
    global Num1Ent
    SubResult = int(Num1Ent.get()) - int(Num2Ent.get())
    Reslbl.config(text="Result: "+str(SubResult))

def Multiply():
    global Num2Ent
    global Num1Ent
    MulResult = int(Num1Ent.get()) * int(Num2Ent.get())
    Reslbl.config(text="Result: "+str(MulResult))

def Divide():
    global Num2Ent
    global Num1Ent
    DivResult = int(Num1Ent.get())//int(Num2Ent.get())
    Reslbl.config(text="Result: "+str(DivResult))

Num1lbl = Label(win,text="1st Number",font=('Calibri',25))
Num1lbl.grid(row=0,column=0)

Num1Ent = Entry(win)
Num1Ent.grid(row=0,column=1)

Num2lbl = Label(win,text="2nd Number",font=('Calibri',25))
Num2lbl.grid(row=1,column=0)

Num2Ent = Entry(win)
Num2Ent.grid(row=1,column=1)

Reslbl = Label(win,text="Result: ",font=('Calibri',25))
Reslbl.grid(row=4,column=0)

Addbtn = Button(win,text="Add",command=Add)
Addbtn.grid(row=3,column=0)

Subbtn = Button(win,text="Subtract",command=Subtract)
Subbtn.grid(row=3,column=1)

Mulbtn = Button(win,text="Multiply",command=Multiply)
Mulbtn.grid(row=3,column=2)

Divbtn = Button(win,text="Divide",command=Divide)
Divbtn.grid(row=3,column=3)

win.geometry('500x500')
win.mainloop()
