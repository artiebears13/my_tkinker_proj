import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo
from source.theme import *


def click_button_open_file(*args, text_field):
    file_path = askopenfilename(
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
    )
    if not file_path:
        return
    with open(file_path, 'r') as input_file:
        text = input_file.read()
        text_field.insert(tk.END, text)


def click_button_save_file(*args, text_field):
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, 'w') as output_file:
        text = text_field.get("1.0", tk.END)
        output_file.write(text)


def create_notepad(frame, theme='white', add_buttons=False):
    frame.configure(bg=theme)
    txt_field = tk.Text(frame, width=49)
    if add_buttons:
        buttons = tk.Frame(frame, bd=2, bg='white')
        button_open_file = tk.Button(buttons, text='Открыть',
                                     command=lambda: click_button_open_file(
                                         text_field=txt_field))
        button_save_file = tk.Button(buttons, text='Сохранить как',
                                     command=lambda: click_button_save_file(
                                         text_field=txt_field
                                     ))

        button_open_file.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
        button_save_file.grid(row=0, column=1, sticky='ew', padx=5)

        buttons.pack(side='top')
    txt_field.pack(side='left')
    txt_field.focus()
    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=txt_field.yview)
    txt_field.configure(yscroll=scrollbar.set)
    scrollbar.pack(side='right', fill='y')
    return txt_field


def pop_up_notebook(theme='white'):
    window = tk.Toplevel()
    window.wm_title("Window")

    menubar = tk.Menu(window, bg='white')
    window.config(menu=menubar)
    file_menu = tk.Menu(menubar)
    # file_menu.add_command(label='New notepad', command=pop_up_notebook)
    # file_menu.add_separator()
    file_menu.add_command(label='Open', command=click_button_open_file)
    # file_menu.add_separator()
    file_menu.add_command(label='Save', command=click_button_save_file)
    # file_menu.add_separator()
    file_menu.add_command(label='Exit', command=window.destroy)
    menubar.add_cascade(
        label="File",
        menu=file_menu,
        background='white'

    )
    # win.geometry('500x500')
    window.configure(bg=theme)

    frame = tk.Frame(window)
    txt_field = create_notepad(frame)
    frame.pack()
    b = ttk.Button(window, text="close", command=lambda: save_and_destroy(window, txt_field))
    b.pack(side='bottom')


def save_and_destroy(window, txt_field):
    click_button_save_file(text_field=txt_field)
    window.destroy()