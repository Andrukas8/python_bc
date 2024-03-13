from tkinter import *

window = Tk()


def submit():
    username = entry.get()
    print(f"Hello {username}")
    entry.config(state=DISABLED)


def delete():
    entry.delete(0, END)


def backspace():
    entry.delete(len(entry.get())-1, END)


entry = Entry(window,
              font=("Arial", 50),
              fg="#00FF00",
              bg="black",
              show="*"
              )

entry.insert(0, "Spongebob")

entry.pack(side=LEFT)

submit_button = Button(window, text="submit",
                       font=("Arial", 50), command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="delete",
                       font=("Arial", 50), command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="backspace",
                          font=("Arial", 50), command=backspace)
backspace_button.pack(side=RIGHT)


window.mainloop()
