from tkinter import *

def create_window():
    #new_window = Toplevel() # new window on top of the other window
    new_window = Tk()        # new_window = Tk() - a new independend window
    old_window.destroy()
     

old_window = Tk()

Button(old_window, text="create new window", command=create_window).pack()

old_window.mainloop()
