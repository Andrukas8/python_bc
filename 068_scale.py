from tkinter import *


def submit():
    print(f"Temperature is {str(scale.get())} degrees C")


window = Tk()

hotLabel = Label(text="🔥",
                 font=("Consolas", 50),
                 fg="red"
                 )
hotLabel.pack()


scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,
              font=("Consolas", 20),
              tickinterval=10,  # adds numeric indicators for value
              # showvalue=0 # hides the current value
              resolution=5,  # increment of a slider
              troughcolor="#69EAFF",
              fg="#FF1C00",
              bg="black"
              )
scale.set(((scale["from"] - scale["to"])/2) + scale["to"])
scale.pack()


coldLabel = Label(text="❄",
                  font=("Consolas", 50),
                  fg="blue"
                  )
coldLabel.pack()


button = Button(window,
                text="submit",
                command=submit)
button.pack()


window.mainloop()
