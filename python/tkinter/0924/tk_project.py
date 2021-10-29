from tkinter import *


def test():
    print("hello")
    display.config(text="Hello world", fg="red", bg="black")


windows = Tk()
windows.title("GUI")

display = Label(windows, text="hi", fg="#3BCCC2", bg="white")
display.pack()
btn = Button(windows, text="click here", command=test)
btn.pack()


windows.mainloop()
