from tkinter import *


def button_clicked():
    dist = float(entry.get())
    print(dist)
    dist = dist * 1.6
    my_label3.config(text=str(dist))


window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

entry = Entry(width=10)
entry.grid(column=1, row=0)


my_label1 = Label(text="Miles", font=("Arial"))
my_label1.grid(column=2, row=0)

my_label2 = Label(text="is equal to ", font=("Arial"))
my_label2.grid(column=0, row=1)

my_label3 = Label(text="0", font=("Arial"))
my_label3.grid(column=1, row=1)

my_label4 = Label(text="Km", font=("Arial"))
my_label4.grid(column=2, row=1)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()
