from tkinter import*
import random as r
print(object)
def random():
    ran = r.randrange(1,7)
    return(ran)
class Process:
    def pack(self):
        global ran
        ran = random()
        lst.insert(0,ran)
        print(lst)
        print("run",ran)
        if ran == 1:
            b1.pack()
        if ran == 2:
            b2.pack(side = TOP)
            print('done')
        if ran == 3:
            b3.pack(side = TOP)
        if ran == 4:
            b4.pack(side = TOP)
        if ran == 5:
            b5.pack(side = TOP)
        if ran == 6:
            b6.pack(side = TOP)
    def forget(self):
        pran = lst[0]
        print('foget',pran)
        if pran == 1:
            b1.forget()
        if pran == 2:
            b2.forget()
        if pran == 3:
            b3.forget()
        if pran == 4:
            b4.forget()
        if pran == 5:
            b5.forget()
        if pran == 6:
            b6.forget()

def run():
    run = Process()
    run.forget()
    run.pack()

lst = [1,1]
root = Tk()
root.geometry("290x325")
root.configure()
tl = Label(root,text='Roll A Dice',font='Arial 30 bold').pack(pady=(0,50))
p1 = PhotoImage(file='dice1.png')
p2 = PhotoImage(file='dice2.png')
p3 = PhotoImage(file='dice4.png')
p4 = PhotoImage(file='dice5.png')
p5 = PhotoImage(file='dice6.png')
p6 = PhotoImage(file='dice7.png')
b1 = Button(image =p1,border =0,command=run)
b1.pack(side = TOP)
b2 = Button(image =p2,border =0,command=run)
b3 = Button(image =p3,border =0,command=run)
b4 = Button(image =p4,border =0,command=run)
b5 = Button(image =p5,border =0,command=run)
b6 = Button(image =p6,border =0,command=run)

can = Canvas(root,width = 290,height=325 )
root.mainloop()
