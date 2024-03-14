from tkinter import *

from tkinter import ttk

window = Tk()

# widget that manages the collection of windows and displays
notebook = ttk.Notebook(window)

tab1 = Frame(notebook)  # new frame for teb1
tab2 = Frame(notebook)

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
# will expand to fill any space not otherwise used, fill="both" will fill space on x and y axis
notebook.pack(expand=True, fill="both")

Label(tab1, text="Hello, this is tab #1", width=50, height=25).pack()
Label(tab2, text="Hello, this is tab #2", width=50, height=25).pack()

window.mainloop()
