# import tkinter
from tkinter import *

# window = tkinter.Tk()
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
# pack method puts the widget into the window
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")


# Button
def button_clicked():
    my_label.config(text=entry.get())
    print("I got Clicked")


button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry (Textbox)
entry = Entry(width=10)
entry.insert(END, string="Some text to display")
entry.pack()
print(entry.get())

# Text (Textarea)
text = Text(height=5, width=30)
# puts cursor in textbox
text.focus()
text.insert(END, "Example of multi-line text entry.")
# Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()


# Spinbox      (textbox with up and down arrow to change integer value using arrows)
def spinbox_used():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale (Slider)


def scale_used(value):
    print(value)


scale = Scale(from_=0, to=10, command=scale_used)
scale.pack()


# Checkbutton (Checkbox)
def checkbutton_used():
    print(checkbutton_state.get())


# variable to hold on to checked state, 0 is off, 1 is on IntVar is class
checkbutton_state = IntVar()
checkbutton = Checkbutton(
    text="Is On?", variable=checkbutton_state, command=checkbutton_used
)
checkbutton_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    # returns value of the radio button checked
    print(radio_state.get())


# Variable to hold on to which radio button is checked
radio_state = IntVar()
radiobutton1 = Radiobutton(
    text="Option1", value=1, variable=radio_state, command=radio_used
)
radiobutton2 = Radiobutton(
    text="Option2", value=2, variable=radio_state, command=radio_used
)
radiobutton1.pack()
radiobutton2.pack()


# Listbox (Contains items in a specific list)
def listbox_used(event):
    # Gets current selection from Listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]

for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()
