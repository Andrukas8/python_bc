from tkinter import *


def submit():
    if (listbox.curselection()):
        food = []
        for index in listbox.curselection():
            food.insert(index, listbox.get(index))
        print("You have ordered:")
        for item in food:
            print(item)


def add():
    if (entryBox.get()):
        listbox.insert(listbox.size(), entryBox.get())
        listbox.config(height=listbox.size())


def delete():
    if (listbox.curselection()):
        for item in reversed(listbox.curselection()):
            listbox.delete(item)
        listbox.config(height=listbox.size())


window = Tk()

# Listbox
listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia", 35),
                  width=12,
                  selectmode=MULTIPLE
                  )
listbox.pack()

listbox.insert(1, "Pizza")
listbox.insert(2, "Pasta")
listbox.insert(3, "Garlic bread")
listbox.insert(4, "Soup")
listbox.insert(5, "Salad")

listbox.config(height=listbox.size())

# Entry Box
entryBox = Entry(window)
entryBox.pack()

addButton = Button(window,
                   text="add",
                   command=add)
addButton.pack()

# Submit Button

submitButton = Button(window,
                      text="submit",
                      command=submit
                      )
submitButton.pack()

# Delete Button

deleteButton = Button(window,
                      text="delete",
                      command=delete
                      )
deleteButton.pack()


window.mainloop()
