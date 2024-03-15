from tkinter import *

speed = 5


def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()-speed)


def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()+speed)


def move_left(event):
    label.place(x=label.winfo_x()-speed, y=label.winfo_y())


def move_right(event):
    label.place(x=label.winfo_x()+speed, y=label.winfo_y())


window = Tk()
window.geometry("500x500")

window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_right)

window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)

label = Label(window, text="🏎", font=("JetBrainsMono NF", 30))
label.place(x=400, y=0)

window.mainloop()
