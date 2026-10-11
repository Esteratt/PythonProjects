from tkinter import *
from tkinter.ttk import *
import random

win = Tk()


def rng():
    global Num1lbl
    global Num2lbl
    Dice1 = random.randint(1,6)
    Num1lbl.config(text=str(Dice1))
    if setting.get()==True:
        Dice2 = random.randint(1,6)
        Num2lbl.config(text=str(Dice2))
        TClbl.config(text="Total: "+str(Dice1+Dice2))
    else:
        Num2lbl.config(text=str(0))

setting = BooleanVar()
setting.trace("w", rng)
setting.set(False)

Ch = Checkbutton(win,text="Add a 2nd dice",var=setting)
Ch.place(x=0,y=125)


Btn = Button(win,text="Roll The Dice",command=rng)
Btn.place(x=0,y=0)

Num1lbl = Label(win,text="0",font=('Calibri',25))
Num1lbl.place(x=0,y=25)

Num2lbl = Label(win,text="0",font=('Calibri',25))
Num2lbl.place(x=50,y=25)

TClbl = Label(win,text="Total: ",font=('Calibri',25))
TClbl.place(x=0,y=75)

win.geometry('300x300')
win.mainloop()