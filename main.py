from tkinter import *


def calcuate():
    miles = float(input1.get())
    km = round(miles * 1.609)
    label3.config(text=km)


window = Tk()
window.title("Mile to Kilometer Convertor")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

input1 = Entry(width=10)
input1.grid(column=2, row=1)
input1.get()

label1 = Label(text="Miles")
label1.grid(column=3, row=1)

label2 = Label(text="is equal to")
label2.grid(column=1, row=2)

label3 = Label(text="0")
label3.grid(column=2, row=2)

label4 = Label(text="Km")
label4.grid(column=3, row=2)

button = Button(text="Calculate", command=calcuate)
button.grid(column=2, row=3)

window.mainloop()
