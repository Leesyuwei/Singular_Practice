from tkinter import *


def conv():
    cm = float(entry_data.get()) * 2.54
    display2.config(text="= %s cm" % str(cm), fg="black", bg="white")


windows = Tk()
windows.title("GUI")

canvas = Canvas(windows, width=200, height=50)
canvas.pack()

display1 = Label(windows, text="inch to cm", fg="black", bg="white")
display1.pack()

entry_data = Entry(windows)
entry_data.pack()

btn = Button(windows, text="caculate", command=conv)
btn.pack()

display2 = Label(windows, text="", fg="black", bg="white")
display2.pack()

windows.mainloop()
