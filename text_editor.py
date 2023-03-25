import pandas as pd
from source.treeview_utilites import *
from source.menu_utilites import *
from source.tab_system import *
from tkinterdnd2 import DND_FILES, TkinterDnD
from source.label_button_frame import *
from source.Figure import *
import multiprocessing


def set_up_window(root_window):
    root_window.configure(background=theme_color)
    root_window.title('Text Editor')
    root_window.geometry('1250x1000')
    root_window.bind('<Control-s>', click_button_save_file)
    root_window.bind('<Control-o>', click_button_save_file)
    root_window.bind('<Escape>', window.destroy)
    # add_scrollbar(root_window, 0, column, rowspan)


def show_info(label, data):
    top_window = tk.Toplevel()
    top_window.wm_title("Window")
    _label = tk.Label(top_window, text=f'{label}:  {data}\n');
    _label.pack()


if __name__ == '__main__':
    theme_color = 'white'
    window = TkinterDnD.Tk()
    set_up_window(window)

    # window = tk.Tk()

    menubar = tk.Menu(window, bg=theme_color)
    window.config(menu=menubar)
    set_up_menu(menubar=menubar, window=window)
    treeview_frame = tk.Frame(window, width=10)
    treeview = Treeview(parent=treeview_frame, row=0, column=0)
    treeview_frame.grid(row=0, column=0)

    print(window.__dir__())
    theme_button = tk.Button(window,
                             text='change theme',
                             command=lambda: change_theme(window))
    tab_system = TabSystem(parent=window, row=1, rowspan=2, column=0)
    theme_button.grid(row=2, column=0)
    # insert_data_frame = UserData(parent=window,
    #                              row=1,
    #                              column=0,
    #                              sticky="nsew")
    # insert_data_frame.add_insert_frame(row=0,
    #                                    column=0,
    #                                    label_text='name',
    #                                    button_text='ok',
    #                                    command=show_info)
    #
    # insert_data_frame.add_insert_frame(row=1,
    #                                    column=0,
    #                                    label_text='surname',
    #                                    button_text='ok',
    #                                    command=show_info)
    # insert_data_frame.add_insert_frame(row=2,
    #                                    column=0,
    #                                    label_text='age',
    #                                    button_text='ok',
    #                                    command=show_info)

    exit_button = tk.Button(window, text="Exit", command=window.destroy)
    exit_button.grid(row=3, column=0, sticky='nsew')

    # window.tk_focusFollowsMouse()
    window.mainloop()
