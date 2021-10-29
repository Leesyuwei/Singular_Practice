from tkinter import *


def cal():
    a = float(entry_data1.get())
    b = float(entry_data3.get())
    if entry_data2.get() == "+":
        ans = a+b
    elif entry_data2.get() == "-":
        ans = a-b
    elif entry_data2.get() == "*":
        ans = a*b
    elif entry_data2.get() == "/":
        ans = a/b
    display4.config(text="= %s" % str(ans), fg="black", bg="white")


windows = Tk()
windows.title("GUI")

canvas = Canvas(windows, width=200, height=75)
canvas.pack()


display1 = Label(windows, text="NUM 1", fg="black", bg="white")
display1.pack()

entry_data1 = Entry(windows)
entry_data1.pack()

display2 = Label(windows, text="calculation", fg="black", bg="white")
display2.pack()

entry_data2 = Entry(windows)
entry_data2.pack()

display3 = Label(windows, text="NUM 2", fg="black", bg="white")
display3.pack()

entry_data3 = Entry(windows)
entry_data3.pack()

display4 = Label(windows, text="", fg="black", bg="white")
display4.pack()


btn = Button(windows, text="calculate", command=cal)
btn.pack()

windows.mainloop()
