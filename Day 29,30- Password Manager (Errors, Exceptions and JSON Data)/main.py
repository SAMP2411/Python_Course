from tkinter import *
from tkinter import messagebox
import pyperclip, json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
import random


def generate_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for item in range(nr_letters)]
    password_symbols = [random.choice(symbols) for item in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for item in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = web_entry.get()
    username = user_entry.get()
    password = pass_entry.get()

    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please make sure you haven't left any fields empty."
        )
    else:
        # is_ok = messagebox.askokcancel(
        #     title=website,
        #     message=f"These are the details entered: \nEmail: {username} \nPassword: {password} \nIs it ok to save?",
        # )

        # if is_ok:
        try:
            with open("data.json", mode="r") as data:
                ### Write to json ###
                # json.dump(new_data, data, indent=4)
                ## Read from Json ###
                # user_data = json.load(data)
                # print(user_data)
                ### Update Data from Json ###
                user_data = json.load(data)  # Reading old data
                user_data.update(new_data)  # Updating old data with new data

        except FileNotFoundError:
            with open("data.json", mode="w") as data:
                json.dump(user_data, data, indent=4)  # Saving Updated Data
                # user_data = f"{website} | {username} | {password} \n"
                # data.write(user_data)

        else:
            with open("data.json", mode="w") as data:
                json.dump(user_data, data, indent=4)  # Saving Updated Data
                # user_data = f"{website} | {username} | {password} \n"
                # data.write(user_data)
        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = web_entry.get()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No Data File Found")

    else:
        if website in data:
            username = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title="Oops",
                message=f"The details for {website} are:\nUsername : {username}\nPassword : {password}",
            )
        else:
            messagebox.showinfo(
                title="Error", message=f"No details for {website} exists."
            )
        web_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)

web_label = Label(text="Website:")
user_label = Label(text="Email/Username:")
pass_label = Label(text="Password:")

web_entry = Entry(width=39)
web_entry.focus()
user_entry = Entry(width=39)
user_entry.insert(0, "samarthp2411@gmail.com")
pass_entry = Entry(width=21)

search_btn = Button(text="Search", command=find_password)
generate_btn = Button(text="Generate Password", command=generate_password)
add_btn = Button(text="Add", width=35, command=save_data)


### Layout Part ###
canvas.grid(row=0, column=1)
web_label.grid(row=1, column=0)
user_label.grid(row=2, column=0)
pass_label.grid(row=3, column=0)

web_entry.grid(row=1, column=1, columnspan=2)
user_entry.grid(row=2, column=1, columnspan=2)
pass_entry.grid(row=3, column=1)

search_btn.grid(row=1, column=2)
generate_btn.grid(row=3, column=2)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
