from tkinter import *

def notepad():
    window = Tk()
    window.title('блокнот')
    window.geometry('300x200')
    txt1 = Entry(window,width=23, font=(50))
    txt1.grid(column=1, row=3)
    window.mainloop()

notepad()
