from tkinter import *


def click():
    if display["text"] == "Green":

        display.config(text="Red", fg="red", bg="white")
    else:
        display.config(text="Green", fg="green", bg="white")


windows = Tk()
windows.title("GUI")


display = Label(windows, text="Green", fg="green", bg="white")
display.pack()
btn = Button(windows, text="click here", command=click)
btn.pack()


windows.mainloop()
