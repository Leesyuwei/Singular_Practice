from tkinter import *


def show():
    display.config(text="Hello world", fg="#3BCCC2", bg="white")


def clear():
    display.config(text="")


windows = Tk()
windows.title("GUI")

display = Label(windows, text="Hello world", fg="#3BCCC2", bg="white")
display.pack()

btn1 = Button(windows, text="show text", command=show)
btn1.pack()
btn2 = Button(windows, text="clear text", command=clear)
btn2.pack()


windows.mainloop()
