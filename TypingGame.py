from tkinter import *
import random
win = Tk()


Timer = 45
Score = 0

Sentlist = ['word', 'isolation', 'tribute', 'package', 'lifestyle', 'collect', 'flavor', 'climb', 'spectrum', 'export', 'corn', 'lesson', 'gift', 'oven', 'card','flow','garbage','danger']

def start(event):
    global Timer
    if Timer == 45:
        countdown()
    NxWord()

def countdown():
    global Timer
    if Timer > 0:
        Timer -= 1
        Timlbl.config(text="Time Left:" + str(Timer))
        Timlbl.after(1000, countdown)

def NxWord():
    global Score
    global Timer
    length = len(Sentlist[1])
    if Timer > 0:
        if TyEnt.get() == Sentlist[1]:
            Score +=length
            Sentlist.remove(Sentlist[1])
        TyEnt.delete(0, END)
        random.shuffle(Sentlist)
        Wordlbl.config(text=str(Sentlist[1]))
        sclbl.config(text='Score:' + str(Score))
        cpslbl.config(text='CPS:' + str((Score / Timer)))

Titlbl = Label(win,text="TYPING GAME",font=('Impact',35), fg='Red')
Titlbl.pack()

Timlbl = Label(win,text="Time Left:",font=('Arial',25))
Timlbl.pack()

sclbl = Label(win,text="Score:",font=('Arial',25))
sclbl.pack()

cpslbl = Label(win,text="CPS:",font=('Arial',25))
cpslbl.pack()

Wordlbl = Label(win,text="word",fg='Red',font=('Arial', 55))
Wordlbl.pack()

TyEnt = Entry(win,font=30)
TyEnt.pack()

Hwlbl = Label(win,text="How to play: Type the word on screen fast",font=('Calibri',24))
Hwlbl.pack()

win.bind('<Return>', start)
win.geometry('800x500')
win.mainloop()
