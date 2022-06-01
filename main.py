from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import string
import random

## characters to generate password from
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generate_random_password():
    ## length of password from the user
    # length = int(input("Enter password length: "))
    len_pass = number_of_symbols.get()
    length = int(len_pass)

    ## shuffling the characters
    random.shuffle(characters)

    ## picking random characters from the list
    password = []
    for i in range(length):
        password.append(random.choice(characters))

    ## shuffling the resultant password
    random.shuffle(password)

    ## converting the list to string
    ## printing the list
    print("".join(password))
    entry_password.delete(0, END)
    entry_password.insert(0, "".join(password))
    window.clipboard_clear()
    window.clipboard_append("".join(password))


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    if website == '' or password == '':
        messagebox.showinfo(title="Oops", message="Please, don't leave any fields empty!")
    else:
        with open("data.txt", "a") as f:
            f.write(f'{website} | {email} | {password}\n')

        entry_website.delete(0, END)
        entry_email.delete(0, END)
        entry_password.delete(0, END)
        entry_email.insert(0, "yourmail@gmail.com")
        messagebox.showinfo(title="Weal done", message="Your password is safe!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0, columnspan=4)

# Label Website
label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

# Label Email/Username
label_email = Label(text="Email/Username:")
label_email.grid(column=2, row=1)

# Label Password
label_password = Label(text="Password:")
label_password.grid(column=0, row=2)

# Label Symbols
label_symbols = Label(text="symbols")
label_symbols.grid(column=4, row=2)

# Generate password Button
generate_pass_button = Button(text="Generate Password", command=generate_random_password)
generate_pass_button.grid(column=2, row=2)

# Spinbox number of symbols
var = IntVar()
var.set(25)
number_of_symbols = Spinbox(window, from_=8, to=25, textvariable=var, width=2)
number_of_symbols.grid(column=3, row=2)

# Add Button
add_button = Button(text="Add", width=60, command=save)
add_button.grid(column=1, row=3, columnspan=4)

# Entry website
entry_website = Entry(width=35)
entry_website.grid(column=1, row=1, columnspan=1)
entry_website.focus()

# Entry email
entry_email = Entry(width=25)
entry_email.grid(column=3, row=1, columnspan=2)
entry_email.insert(0, "yourmail@gmail.com")

# Entry password
entry_password = Entry(width=35)
entry_password.grid(column=1, row=2)

window.mainloop()
