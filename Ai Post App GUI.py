from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Automation App")
window.geometry("700x400")

# Create a Frame + Content Frame with scrollbar
frame = Frame(window, bg='white', width=1000, height=700)
frame.pack(fill=BOTH, expand=True)
canvas = Canvas(frame)
canvas.pack(side=LEFT, fill=BOTH, expand=True)
canvas.bind_all("<MouseWheel>", lambda event:on_mousewheel(event))  # Labda have to use when function is below
scrollbar = Scrollbar(frame, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
content_frame = Frame(canvas)
canvas.create_window((0, 0), window=content_frame, anchor=NW)


# website info widgets
webinfo_frame = LabelFrame(content_frame, text="Input your website information")
webinfo_frame.grid(row=0, column=0, pady=10, padx=20, sticky='w')

website_name = Label(webinfo_frame, text="Website Name", font=15)
website_name.grid(row=0, column=0, padx=10, pady=3)

user_name = Label(webinfo_frame, text="User Name", font=15)
user_name.grid(row=0, column=1, padx=10, pady=3)

app_pass = Label(webinfo_frame, text="Application Password", font=1)
app_pass.grid(row=0, column=2, padx=10, pady=3)

website_entry = Entry(webinfo_frame, font=15)
website_entry.insert(0, "edmontonranked.ca")  # Default data
website_entry.grid(row=1, column=0, padx=10, pady=10)

username_entry = Entry(webinfo_frame, font=15)
username_entry.insert(0, "info@updigital.ca")
username_entry.grid(row=1, column=1, padx=10, pady=10)

app_pass_entry = Entry(webinfo_frame, font=10)
app_pass_entry.insert(0, "pXHi KFT4 A7dm JUO5 JaXz r2gY")
app_pass_entry.grid(row=1, column=2, padx=10, pady=10)


# Webiste info Operation
operation_label = Frame(content_frame)
operation_label.grid(row=2,column=0,sticky="w")

category = Entry(operation_label, width=15)
category.insert(0, 'Category Name..')
category.grid(row=3, column=3, sticky='w', pady=6, padx=5, ipadx=5, ipady=5)

status = ttk.Combobox(operation_label, width=12, values=['Draft', 'Publish'], state='readonly')
status.set('Draft')
status.grid(row=3, column=4,sticky='w', pady=6, padx=5, ipadx=5, ipady=5)

outline_numbers_label = Label(operation_label, text="Outline Number : ")
outline_numbers_label.grid(row=3, column=5, sticky='w', pady=6, padx=5, ipadx=5, ipady=5)
outline_numbers = Spinbox(operation_label, width=1, from_= 5, to=50)
outline_numbers.grid(row=3, column=6, sticky='w', pady=6, padx=1, ipadx=2, ipady=5)


# Terminal
terminal = LabelFrame(content_frame, text="Terminal")
terminal.grid(row=4, column=0, pady=10)

keyword_label = Label(terminal, text="Input Keywords")
keyword_label.grid(row=5, column=0, pady=5)

keyword_input = Text(terminal)
keyword_input.config(height=15, width=40)
keyword_input.insert('1.0', "Input keyword list here...")
keyword_input.grid(row=6, column=0, pady=10)

output_label = Label(terminal, text="Output")
output_label.grid(row=5, column=1, pady=5)

output = Text(terminal, bg='#3F4247', fg='white')
output.config(height=15, width=40)
output.grid(row=6, column=1, pady=10)


# Command
command_label = Frame(content_frame)
command_label.grid(row=7,column=0)

start = Button(command_label, text="Run", font=15, bg='#20B2AA', fg='white', command=lambda:operation_start()) # Labda have to use when function is below
start.grid(row=8, column=0, sticky='w', padx=20, pady=20, ipadx=20)

stop = Button(command_label, text='Stop', font=15, bg='#CC397B', fg='white')
stop.grid(row=8, column=1, sticky='w', padx=20, pady=20, ipadx=20)


def operation_start():
    website_name = website_entry.get()
    username = username_entry.get()
    app_pass = app_pass_entry.get()
    category_name = category.get()
    status_value = status.get()
    outline_numbers_value = outline_numbers.get()
    keyword_list = keyword_input.get('1.0', END)

    output.insert(1.0, 'Website Name: ' + website_name + '\n')
    output.insert(1.0, 'User Name: ' + username + '\n')
    output.insert(1.0, 'App Password: ' + app_pass + '\n')
    output.insert(1.0, 'Category Name: ' + category_name + '\n')
    output.insert(1.0, 'Status: ' + status_value + '\n')
    output.insert(1.0, 'Outline Numbers: ' + outline_numbers_value + '\n')
    output.insert(1.0, 'Keyword: ' + keyword_list + '\n')

def on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

if __name__== '__main__':
    window.mainloop()
