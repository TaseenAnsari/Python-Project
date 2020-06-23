from tkinter import *
import random as r
class Dice:
    def __init__(self):
        root.geometry('240x240')
        tittle = Label(root,text='Rolling a Dice',bg='red',fg='yellow').pack()

    def random(b):
        ran = r.randrange(1, 7)
        c =Dice()
        c.button(ran)

    def button(n):
        ran1 = n
        p1 = PhotoImage(file="dice1.png")
        p2 = PhotoImage(file="dice2.png")
        p3 = PhotoImage(file="dice4.png")
        p4 = PhotoImage(file="dice5.png")
        p5 = PhotoImage(file="dice6.png")
        p6 = PhotoImage(file="dice7.png")
        if ran1 == 1:
            b1 = Button(root,image=p1,command=random).pack()
        if ran1 == 2:
            b1 = Button(root,image=p2,command=random).pack()
        if ran1 == 3:
            b1 = Button(root,image=p3,command=random).pack()
        if ran1 == 4:
            b1 = Button(root,image=p4,command=random).pack()
        if ran1 == 5:
            b1 = Button(root,image=p5,command=random).pack()
        if ran1 == 6:
            b1 = Button(root,image=p6,command=random).pack()



root = Tk()
run = Dice()
root.mainloop()