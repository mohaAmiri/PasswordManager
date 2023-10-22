from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button

""" Window Setup """
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
log_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=log_img)
canvas.grid(row=0, column=1)

""" Labels """
website_label = Label(text="website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

""" Entries """
website_entry = Entry(width=30)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=48)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "mohammad@gmail.com")

password_entry = Entry(width=30)
password_entry.grid(row=3, column=1)

""" Button """
search_button = Button(text="search", width=15)
search_button.grid(row=1, column=2)

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)

add_button = Button(text="add", width=42)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
