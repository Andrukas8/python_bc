from tkinter import *


def display():
    if (x.get() == 1):
        print("You agree!")
    else:
        print("You don't agree!")


window = Tk()

x = IntVar()

python_photo = PhotoImage(file="Python-logo-notext.png")

check_button = Checkbutton(window,
                           text="Agree to something good",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=("Arial", 20),
                           fg="#00FF00",
                           bg="black",
                           activeforeground="#00FF00",
                           activebackground="black",
                           padx=25,
                           pady=10,
                           image=python_photo,
                           compound="left"
                           )

check_button.pack()


window.mainloop()
