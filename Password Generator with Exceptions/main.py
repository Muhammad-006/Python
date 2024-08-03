from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
COLOR = '#F6F5F5'
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def search_website():
    try:
        with open('Password Manager.json', mode='r') as file:
            found = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo('Oops', message = 'File not available')
    else:
        try:
            email = found[website_input.get()]['Email']
            word = found[website_input.get()]['Password']
        except KeyError:
            messagebox.showinfo('Oops', message='No data to show')
        else:
             messagebox.showinfo('Website = {website_input.get()}',
                                 message = f'Email = {email}\n Password = {word}')

def create_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    
    char_list = [random.choice(letters) for char in range(nr_letters)]
    symbol_list = [random.choice(symbols) for char in range(nr_symbols)]
    number_list = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = char_list + symbol_list + number_list
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(END, f'{password}')
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_to_file():
    website = website_input.get()
    email = email_user_input.get()
    word = password_input.get()
    data = {
        website: {
            'Email': email,
            'Password': word
        }
    }
    if website != '' and email != '' and word != '':
        done = messagebox.askokcancel(title = 'Information', message =
        f'Your information is:\nWebsite: {website}\nEmail: {email}\nPassword: {word}\nDo you want to save?')

        if done:
            try:
                with open('Password Manager.json', mode='r') as file:
                    update_data = json.load(file)
            except:
                with open('Password Manager.json', mode = 'w') as file:
                    json.dump(data, file, indent = 4)
            else:
                update_data.update(data)
                with open('Password Manager.json', mode = 'w') as file:
                    json.dump(update_data, file, indent = 4)
            finally:
                website_input.delete(0,END)
                password_input.delete(0, END)


    else:
        messagebox.showinfo(title='Alert!', message="Don't leave any fields empty")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx = 50, pady = 50, bg = COLOR)

logo_img = PhotoImage(file = 'logo.png')
canvas = Canvas(width = 200, height = 200)
canvas.create_image(100, 100, image = logo_img)
canvas.config(bg = COLOR, highlightthickness = 0)
canvas.grid(column = 1, row = 0)


website_label = Label(text = 'Website:', font = ('Courier', 12, 'normal'), bg = COLOR, pady = 5)
website_label.grid(column = 0, row = 1)


email_user = Label(text = 'Email/User Name', font = ('Courier', 12, 'normal'), bg = COLOR, pady = 5)
email_user.grid(column = 0, row = 2)

password_label = Label(text = 'Password', font = ('Courier', 12, 'normal'), bg = COLOR, pady = 5)
password_label.grid(column = 0, row = 3)

email_user_input = Entry(width = 45)
email_user_input.insert(END, 'Muhammad@gmail.com')
email_user_input.grid(row = 2, column = 1, columnspan = 2, sticky = 'ew',padx = 10, pady = 5)

website_input = Entry(width = 20)
website_input.focus()
website_input.grid(row = 1, column = 1, sticky ='ew', padx = 10, pady = 5)

password_input = Entry(width = 20)
password_input.grid(row = 3, column = 1, sticky ='ew', padx = 10, pady = 5)

generate_password = Button(text = 'Generate Password', bg = '#FFDE4D', command = create_password)
generate_password.grid(column = 2, row = 3)

add_button = Button(text ='add', width = 45, bg = '#FFB22C', command = save_to_file)
add_button.grid(row = 4, column = 1, columnspan = 2, sticky = 'ew',padx = 10, pady = 5)

search_button = Button(text = 'Search', bg = '#FFDE4D', width = 14, command = search_website)
search_button.grid(column = 2, row = 1)
window.mainloop()