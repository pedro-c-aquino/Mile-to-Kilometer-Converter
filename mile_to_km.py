from tkinter import *


def calculate():
    mile = float(entry.get())
    res = round(mile * 1.6)
    result.config(text=f"{res}")
    return res


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

entry = Entry(width=7, justify="right")
entry.grid(column=1, row=0)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

result = Label(text="0")
result.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()
