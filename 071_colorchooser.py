from tkinter import *
from tkinter import colorchooser  # submodule


def click():
    color = colorchooser.askcolor()
    colorHex = color[1]
    window.config(bg=colorHex)


window = Tk()
window.geometry("410x420")

button = Button(text="Click Me",
                command=click
                )
button.pack()

window.mainloop()
