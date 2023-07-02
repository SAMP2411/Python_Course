from tkinter import *


def button_clicked():
    my_label.config(text=entry.get())
    print("I got Clicked")


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=5, row=5)
my_label.config(padx=50, pady=50)

button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=0, row=0)

entry = Entry(width=10)
print(entry.get())
# entry.pack()
entry.grid(column=250, row=2)

window.mainloop()
