from tkinter import *
import time


def click():
    if display["text"] == "POP":
        # pop_img = canvas.create_image(300, 300, image=img)
        # msg = canvas.create_text(300, 100, text="",
        #                          fill="white", font=("Arial", 30))
        canvas.delete()

        pop_img = canvas.create_image(
            300, 300, image=img2)
        msg = canvas.create_text(300, 100, text="POP",
                                 fill="white", font=("Arial", 30))
        display.config(text="", fg="red", bg="white")
    else:
        canvas.delete()
        pop_img = canvas.create_image(
            300, 300, image=img)
        display.config(text="POP", fg="red", bg="white")
        # canvas.destroy()

        # def move_canvas(event):
        #     key = event.keysym
        #     print(key)
        #     if key == "w":
        #         canvas.move(msg, 0, -10)
        #     elif key == "s":
        #         canvas.move(msg, 0, 10)
        #     elif key == "a":
        #         canvas.move(msg, -10, 0)
        #     elif key == "d":
        #         canvas.move(msg, 10, 0)


windows = Tk()
windows.title("GUI")

canvas = Canvas(windows, width=600, height=600)
canvas.pack()

windows.iconbitmap("./no_pop.ICO")

img = PhotoImage(file="./no_pop.PNG")
img2 = PhotoImage(file="./pop.PNG")
pop_img = canvas.create_image(300, 300, image=img)


# msg = canvas.create_text(300, 100, text="",
#                          fill="white", font=("Arial", 30))

# canvas.bind_all("<Key>", move_canvas)

display = Label(windows, text="POP", fg="green", bg="white")
display.pack()
btn = Button(windows, text="click to pop", command=click)
btn.pack()


windows.mainloop()
