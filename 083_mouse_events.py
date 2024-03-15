from tkinter import *


def doSomething(event):
    print(f"Mouse coordinates {str(event.x)}, {str(event.y)}")


window = Tk()


# window.bind("<Button-1>", doSomething) # Left mouse button
# window.bind("<Button-2>", doSomething) # Pressing the scroll wheel
# window.bind("<Button-3>", doSomething) # Right mouse button
# window.bind("<ButtonRelease>", doSomething) # on mouse release
# window.bind("<Leave>", doSomething) # on mouse leaving
window.bind("<Motion>", doSomething)  # where the mouse moved

window.mainloop()
