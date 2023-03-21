import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinterdnd2 import DND_FILES, TkinterDnD
from pathlib import Path


class Treeview(ttk.Treeview):
    def __init__(self, *, parent,
                 row: int = 0,
                 column: int = 0,
                 rowspan: int = 1,
                 columns: set = ('parameter', 'value')):
        super().__init__(parent, columns=columns, show='headings', height=10, selectmode='browse')
        self.heading('parameter', text='Параметр')
        self.heading('value', text='Значение')
        self.data = []

        self.init_data()
        self.add_scrollbar(parent, row, column, rowspan)
        self.stored_dataframe = pd.DataFrame()
        self.drop_target_register(DND_FILES)
        self.dnd_bind("<<Drop>>", self.detect)
        self.grid(row=row, rowspan=rowspan, column=column, sticky='wsew')

    def detect(self, event):
        files = event.data
        for file in files:
            print(file)

    def add_scrollbar(self, parent, row, column, rowspan):
        scrollbar = ttk.Scrollbar(parent, orient=tk.VERTICAL, command=self.yview)
        self.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=row, rowspan=rowspan, column=column + 1, sticky='ns')

    def init_data(self):
        for i in range(1, 100):
            self.data.append((f'параметр {i}', i))
        for data in self.data:
            self.insert('', 'end', values=data)


def set_up_window(root_window):
    root_window.configure(background=theme_color)
    root_window.title('Text Editor')
    root_window.geometry('1000x1000')


if __name__ == '__main__':
    theme_color = 'white'
    window = TkinterDnD.Tk()
    set_up_window(window)

    treeview = Treeview(parent=window,row=0,column=0)
    treeview.focus()
    window.mainloop()