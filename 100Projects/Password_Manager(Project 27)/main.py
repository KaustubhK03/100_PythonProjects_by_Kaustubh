from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json
# ---------------------------- CONSTANTS ------------------------------- #
FONT = ("cornier", 15)
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '{', '}', '@', '^', '_', '-', '?']


# ---------------------------- SEARCHING PASSWORD FUNCTION ------------------------------- #
def search_my_password():
    try:
        with open("data.json", "r") as pass_file:
            data_dict = json.load(pass_file)
            website = web_entry.get().title()
            messagebox.showinfo(title=website, message=f"Email: {data_dict[website]['Email']}\n"
                                                       f"Password: {data_dict[website]['Password']}")
    except FileNotFoundError:
        messagebox.showerror(title="Error!", message="No Datafile found.")
    except KeyError:
        messagebox.showerror(title="Error", message=f"No details for the website {website} exists.")


# ---------------------------- PASSWORD GENERATOR FUNCTION ------------------------------- #
def pass_generator():
    letter_list = [choice(LETTERS) for _ in range(randint(1, 5))]
    num_list = [choice(NUMBERS) for _ in range(randint(0, 4))]
    symbols_lst = [choice(SYMBOLS) for _ in range(randint(2, 4))]

    combined_choices_list = letter_list + num_list + symbols_lst
    shuffle(combined_choices_list)

    password = "".join(combined_choices_list)
    pw_entry.delete(0, END)
    pw_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD FUNCTION ------------------------------- #
def save_info():
    website = web_entry.get()
    email = email_entry.get()
    password = pw_entry.get()
    new_data = {website: {
            "Email": email,
            "Password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading the current data in json file
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating the current data in that dictionary
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Writing the new data
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            pw_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas setup
canvas = Canvas(width=200, height=200)
lock_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_png)
canvas.grid(column=1, row=0)

# The Website label
web_label = Label(text="Website:", font=FONT)
web_label.grid(column=0, row=1)

# The Website's Entry
web_entry = Entry(width=21)
web_entry.focus()
web_entry.grid(column=1, row=1)

# The search Button
search_button = Button(text="Search", width=13, command=search_my_password)
search_button.grid(column=2, row=1)

# The email/Username Label
email_user = Label(text="Email/Username:", font=FONT)
email_user.grid(column=0, row=2)

# The email Entry
email_entry = Entry(width=38)
email_entry.insert(0, "kalambkarkaustubh@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

# The password Label
pw = Label(text="Password:", font=FONT)
pw.grid(column=0, row=3)

# The password entry
pw_entry = Entry(width=21)
pw_entry.grid(column=1, row=3)

# The generate Button
gene = Button(text="Generate Password", command=pass_generator)
gene.grid(column=2, row=3)

# The Add Button
add_button = Button(text="Add", width=36, command=save_info)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
