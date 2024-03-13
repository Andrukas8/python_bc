from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# window = serves as a container for widgets

window = Tk()  # instantiate and instance of a windows for us
window.geometry("420x420")
window.title("Bro Code first GUI program")

icon = PhotoImage(file='Python-logo-notext.png')
window.iconphoto(True, icon)
window.config(background="#5cfcff")

window.mainloop()
