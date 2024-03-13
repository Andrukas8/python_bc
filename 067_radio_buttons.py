from tkinter import *

food = ["pizza", "hamburger", "hotdog"]


def order():
    if x.get() == 0:
        print("You ordered Pizza")
    elif x.get() == 1:
        print("You ordered a hamburger")
    elif x.get() == 2:
        print("You ordered a hotdog")
    else:
        print("huh?")


window = Tk()
x = IntVar()

image = PhotoImage(file="Python-logo-notext.png")

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],  # adds text
                              variable=x,  # groups rb together if they chare the same variable
                              value=index,  # asignes each radiobutton a different value
                              padx=25,  # adds padding
                              pady=25,
                              font=("Impact", 50),
                              image=image,
                              compound=LEFT,
                              justify=LEFT,
                              indicatoron=0,
                              width=375,
                              command=order
                              )
    radiobutton.pack(anchor=W)


window.mainloop()
