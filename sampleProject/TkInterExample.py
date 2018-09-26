from tkinter import *


def clicked():
    res = "Hello " + txt.get()
    lbl.configure(text=res)


window = Tk()
window.title("TkInter Hello World")
window.geometry('350x60')

lbl = Label(window, text="Enter Your Name")
lbl.grid(column=0, row=0)

txt = Entry(window, width=30)
txt.grid(column=0, row=1)

btn = Button(window, text="Submit", command=clicked)
btn.grid(column=1, row=1)

window.mainloop()
