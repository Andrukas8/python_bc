"""
convertins .py into an executable: pip and pyinstaller are installed/updated
- collect all app code into one folder
- image for icon has to be converted into .ico (use icoconvert.com)
- using terminal cd into this folder
- in terminal run:
pyinstaller ...
                -F (all in 1 file)
                -w (removes terminal window)
                -i icon.ico (adds custom icon to python file)
                clock.py (name of the main python file)
.exe is located in the dist folder
"""

from tkinter import *
from time import *


def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d %Y")
    date_label.config(text=date_string)

    window.after(1000, update)


window = Tk()

time_label = Label(window,
                   font=("Arial", 50),
                   fg="#00FF00",
                   bg="black"
                   )
time_label.pack()

day_label = Label(window,
                  font=("Ink Free", 25),
                  )
day_label.pack()

date_label = Label(window,
                   font=("Ink Free", 30),
                   )
date_label.pack()

update()

window.mainloop()
