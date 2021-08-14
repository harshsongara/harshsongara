import tkinter
from tkinter import messagebox
import random
import pyperclip
import json

FONT = ('Ariar', 10)
BLUE = '#3EE5E1'
OBLUE = '#AEF5F3'


# ------------------------------SEARCH-------------------------------------------#


def search():
    get_website = website_entry.get()
    try:
        with open('data.json') as file:
            data = json.load(file)
        source = [item for key, item in data[get_website].items()]
        messagebox.showinfo(title=get_website, message=f"Username: {source[0]}\nPassword: {source[1]}")
    except:
        messagebox.showinfo(title=get_website, message=f"No data found")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def password_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for n in range(random.randint(8, 10))]
    password_list += [random.choice(numbers) for n in range(random.randint(2, 4))]
    password_list += [random.choice(symbols) for n in range(random.randint(2, 4))]

    random.shuffle(password_list)
    password = ''.join(password_list)

    password_entry.delete(0, 'end')
    password_entry.insert(0, password)
    pyperclip.copy(password)
    # print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_pw():
    get_website = website_entry.get()
    get_username = user_name_entry.get()
    get_pw = password_entry.get()
    data_dict = {get_website:
                     {"username": get_username,
                      "password": get_pw
                      }
                 }

    if get_website == '' or get_username == '' or get_pw == '':
        messagebox.showinfo(title='Oops', message='Please complete all the fields')
    else:
        is_ok = messagebox.askokcancel(title=get_website,
                                       message=f'This are the details\nEmail: {get_username}\nPassword {get_pw}')
        if is_ok:
            try:
                # Reading
                with open('data.json', 'r') as file:
                    data = json.load(file)

                    # print(data)
            except:
                # Creation
                print('Exception raised')
                with open('data.json', 'w') as file:
                    json.dump(data_dict, file, indent=4)
            else:
                # Updating
                data.update(data_dict)
                with open('data.json', 'w') as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, 'end')
                password_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title('Password Manager')
window.config(padx=50, pady=50, bg=BLUE)

photo_image = tkinter.PhotoImage(file='logo.png')
canvas = tkinter.Canvas(width=200, height=200, bg=BLUE, highlightthickness=0)
canvas.create_image(100, 100, image=photo_image)
canvas.grid(column=1, row=0)

website = tkinter.Label(text='Website:', font=FONT, bg=BLUE)
website_entry = tkinter.Entry(width=34, bg=OBLUE)
website.grid(column=0, row=1, sticky='W', padx=30)
website_entry.grid(column=1, row=1, sticky='W')
website_entry.focus()

user_name = tkinter.Label(text='Email/Username:', font=FONT, bg=BLUE)
user_name_entry = tkinter.Entry(width=34, bg=OBLUE)
user_name_entry.insert(0, 'harshsongara@gmail.com')
user_name.grid(column=0, row=2, sticky='W', padx=30)
user_name_entry.grid(column=1, row=2, sticky='W')

password = tkinter.Label(text='Password:', font=FONT, bg=BLUE)
password_entry = tkinter.Entry(width=34, bg=OBLUE, fg='#0D8885')
password.grid(column=0, row=3, sticky='W', padx=30)
password_entry.grid(column=1, row=3, sticky='W')

generate_button = tkinter.Button(text='Generate Password', font=FONT, command=password_generate, bg='#35BCB8')
# password_generate()
generate_button.grid(column=2, row=3)
add_button = tkinter.Button(text='Add', width=21, command=save_pw, bg='#35BCB8')
add_button.grid(column=1, row=4, sticky='W')

search_button = tkinter.Button(text='Search', command=search, bg='#35BCB8')
search_button.grid(column=2, row=1, sticky='W')

window.mainloop()
