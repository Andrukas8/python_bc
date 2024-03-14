from tkinter import *


def openFile():
    print("File has been opened")


def saveFile():
    print("File has been saved")


def cut():
    print("Cust something in the file")


def copy():
    print("Copied something in the file")


def paste():
    print("Pasted something in the file")


window = Tk()

openImage = PhotoImage(file="Python-logo-notext.png")

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0, font=("MV Boli", 15))
menubar.add_cascade(label="File", menu=fileMenu)  # drop down menu effect
fileMenu.add_command(label="Open", command=openFile,
                     image=openImage, compound=LEFT)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit)

editMenu = Menu(menubar, tearoff=0, font=("MV Boli", 15))
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)

window.mainloop()
