import tkinter as tk
from source.notepad import *


def set_up_menu(*, menubar, window):
    file_menu = tk.Menu(menubar)
    file_menu.add_command(label='New notepad', command=pop_up_notebook)
    # file_menu.add_separator()
    # file_menu.add_command(label='Open', command=click_button_open_file)
    # file_menu.add_separator()
    # file_menu.add_command(label='Save', command=click_button_save_file)
    # file_menu.add_separator()
    file_menu.add_command(label='Exit', command=window.destroy)

    menubar.add_cascade(
        label="File",
        menu=file_menu,
        background='white'

    )

    help_menu = tk.Menu(
        menubar,
        tearoff=0
    )
    help_menu.add_command(label='Shotcuts', command=show_shortcuts)
    help_menu.add_command(label='About...')
    menubar.add_cascade(label='Help', menu=help_menu)


def show_shortcuts():
    win = tk.Toplevel()
    win.wm_title("Window")
    win.geometry('200x200')

    l = tk.Label(win, text="'Ctrl+s' to save file\n 'Ctrl+O' to open file")
    l.grid(row=0, column=0)

    b = ttk.Button(win, text="Okay", command=win.destroy)
    b.grid(row=1, column=0)
