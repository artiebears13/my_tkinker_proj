import pandas as pd
from source.treeview_utilites import *
from source.menu_utilites import *
from source.tab_system import *
from tkinterdnd2 import DND_FILES, TkinterDnD


# def table_viewer(table: ttk.Treeview, dataframe: pd.DataFrame):
#     scroll_Y = tk.Scrollbar(frame, orient='vertical', command=frame.yview)
#     scroll_X = tk.Scrollbar(frame, orient='horizontal', command=frame.xview)
#     table.configure(yscrollcommand=scroll_Y.set, xscrollcommand=scroll_X.set)
#     scroll_Y.pack(side="right", fill="y")
#     scroll_X.pack(side="bottom", fill="x")
#     table.stored_dataframe = dataframe
#     columns = list(dataframe.columns)
#     table.__setitem__('column', columns)
#     table.__setitem__('show', columns)
#     for col in columns:
#         table.heading(col, text=col)
#
#     rows = dataframe.


def set_up_window(root_window):
    root_window.configure(background=theme_color)
    root_window.title('Text Editor')
    root_window.geometry('1000x1000')
    root_window.bind('<Control-s>', click_button_save_file)
    root_window.bind('<Control-o>', click_button_save_file)
    root_window.bind('<Escape>', window.destroy)




if __name__ == '__main__':
    theme_color = 'white'

    # window = tk.Tk()
    window = TkinterDnD.Tk()
    set_up_window(window)

    menubar = tk.Menu(window, bg=theme_color)
    window.config(menu=menubar)
    set_up_menu(menubar=menubar, window=window)

    # treeview_frame = tk.Frame(window, bg=theme_color)
    treeview = Treeview(parent=window,row=0,column=0)

    # treeview_frame2 = tk.Frame(window, bg=theme_color)
    # create_treeview(treeview_frame2)

    # notepad.grid(row=0, rowspan=2, column=1, sticky='nsew')

    print(window.__dir__())
    # print(window.winfo_children()[0].configure(bg='black'))

    # tab_system = ttk.Notebook(window)
    # tab_txt = tk.Frame(tab_system)
    # tab_csv = tk.Frame(tab_system)
    # create_notepad(tab_txt)
    #
    # tab_system.add(tab_txt, text='txt')
    # tab_system.add(tab_csv, text='csv')

    # frame_theme_button = tk.Frame(window)
    theme_button = tk.Button(window, text='change theme', command=lambda: change_theme(window))
    # treeview_frame.grid(row=0, column=0, sticky='ns')
    # treeview_frame2.grid(row=1, column=0, sticky='s')
    # tab_system.grid(row=0, rowspan=2, column=1)
    tab_system = TabSystem(parent=window,row=0, rowspan=2, column=1)
    theme_button.grid(row=3, column=0)
    # print(notepad.winfo_children()[0].widgetName, type(notepad.winfo_children()[0].widgetName))
    # print(dir(tk))

    window.tk_focusFollowsMouse()
    window.mainloop()
