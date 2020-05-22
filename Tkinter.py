from tkinter import *
from tkinter import ttk
from tkinter import messagebox

ActivePlayer=1        #active player
p1=[]                  #What player selected
p2=[]                   #What player selected
count = 0

root=Tk()
root.iconbitmap("tictac.ico")
root.title("Tic Tac Toe : Player 1")
style=ttk.Style()
style.theme_use('classic')

bu1=ttk.Button(root,text=' ')
bu1.grid(row=0 , column=0,sticky='snew', ipadx=40 , ipady=40)
bu1.config(command=lambda : BuClick(1))

bu2=ttk.Button(root,text=' ')
bu2.grid(row=0 , column=1,sticky='snew', ipadx=40 , ipady=40)
bu2.config(command=lambda : BuClick(2))

bu3=ttk.Button(root,text=' ')
bu3.grid(row=0 , column=2,sticky='snew', ipadx=40 , ipady=40)
bu3.config(command=lambda : BuClick(3))

bu4=ttk.Button(root,text=' ')
bu4.grid(row=1 , column=0,sticky='snew', ipadx=40 , ipady=40)
bu4.config(command=lambda : BuClick(4))

bu5=ttk.Button(root,text=' ')
bu5.grid(row=1 , column=1,sticky='snew', ipadx=40 , ipady=40)
bu5.config(command=lambda : BuClick(5))

bu6=ttk.Button(root,text=' ')
bu6.grid(row=1 , column=2,sticky='snew', ipadx=40 , ipady=40)
bu6.config(command=lambda : BuClick(6))

bu7=ttk.Button(root,text=' ')
bu7.grid(row=2 , column=0,sticky='snew', ipadx=40 , ipady=40)
bu7.config(command=lambda : BuClick(7))

bu8=ttk.Button(root,text=' ')
bu8.grid(row=2 , column=1,sticky='snew', ipadx=40 , ipady=40)
bu8.config(command=lambda : BuClick(8))

bu9=ttk.Button(root,text=' ')
bu9.grid(row=2 , column=2,sticky='snew', ipadx=40 , ipady=40)
bu9.config(command=lambda : BuClick(9))


def BuClick(id):
    global ActivePlayer
    global p1
    global p2
    if (ActivePlayer==1):
        SetLayout(id,'X')
        p1.append(id)
        root.title('Tic Tac Toe : Player 2')
        ActivePlayer=2
    elif (ActivePlayer==2):
        SetLayout(id,'O')
        p2.append(id)
        root.title('Tic Tac Toe : Player 1')
        ActivePlayer=1
    Checkwinner()


def SetLayout(id,text):
    global count
    if (id==1):
        bu1.config(text=text)
        bu1.state(['disabled'])
        count +=1
    elif (id == 2):
        bu2.config(text=text)
        bu2.state(['disabled'])
        count += 1
    elif (id == 3):
        bu3.config(text=text)
        bu3.state(['disabled'])
        count += 1
    elif (id == 4):
        bu4.config(text=text)
        bu4.state(['disabled'])
        count += 1
    elif (id == 5):
        bu5.config(text=text)
        bu5.state(['disabled'])
        count += 1
    elif (id == 6):
        bu6.config(text=text)
        bu6.state(['disabled'])
        count += 1
    elif (id == 7):
        bu7.config(text=text)
        bu7.state(['disabled'])
        count += 1
    elif (id == 8):
        bu8.config(text=text)
        bu8.state(['disabled'])
        count += 1
    elif (id == 9):
        bu9.config(text=text)
        bu9.state(['disabled'])
        count += 1

def Checkwinner():
    winner = -1
    if (1 in p1 and 2 in p1 and 3 in p1):
        winner = 1
    elif (1 in p2 and 2 in p2 and 3 in p2):
        winner = 2
    elif (4 in p1 and 5 in p1 and 6 in p1):
        winner = 1
    elif (4 in p2 and 5 in p2 and 6 in p2):
        winner = 2
    elif (7 in p1 and 8 in p1 and 9 in p1):
        winner = 1
    elif (7 in p2 and 8 in p2 and 9 in p2):
        winner = 2
    elif (1 in p1 and 4 in p1 and 7 in p1):
        winner = 1
    elif (1 in p2 and 4 in p2 and 7 in p2):
        winner = 2
    elif (2 in p1 and 5 in p1 and 8 in p1):
        winner = 1
    elif (2 in p2 and 5 in p2 and 8 in p2):
        winner = 2
    elif (3 in p1 and 6 in p1 and 9 in p1):
        winner = 1
    elif (3 in p2 and 6 in p2 and 9 in p2):
        winner = 2
    elif (1 in p1 and 5 in p1 and 9 in p1):
        winner = 1
    elif (1 in p2 and 5 in p2 and 9 in p2):
        winner = 2
    elif (3 in p1 and 5 in p1 and 7 in p1):
        winner = 1
    elif (3 in p2 and 5 in p2 and 7 in p2):
        winner = 2
    elif (count == 9):
        winner = 3

    if winner == 1:
        messagebox.showinfo(title='Congrats', message=' Player 1 is winner')
    if winner == 2:
        messagebox.showinfo(title='Congrats', message=' Player 2 is winner')
    if winner == 3:
        messagebox.showinfo(title='Congrats', message=' TIE')

root.mainloop()