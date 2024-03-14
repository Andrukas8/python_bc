from tkinter import *
from tkinter import filedialog


def saveFile():
    file = filedialog.asksaveasfile(initialdir="./",
                                    title="Open File",
                                    filetypes=[
                                        ("Text file", "*.txt"),
                                        ("HTML file", "*.html"),
                                        ("All files", "*.*")
                                    ])
    if file is None:
        return
    fileText = str(text.get(1.0, END))
    file.write(fileText)
    file.close()


window = Tk()

button = Button(window,
                text="save",
                command=saveFile
                )
button.pack()

text = Text(window,
            bg="light yellow",
            font=("Ink Free", 25),
            height=8,
            width=20,
            padx=20,
            pady=20,
            fg="purple"
            )
text.pack()

window.mainloop()
