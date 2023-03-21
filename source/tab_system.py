import pandas as pd
from source.treeview_utilites import *
from source.menu_utilites import *
from tkdnd import DND_FILES, TkinterDnD


class TabSystem(ttk.Notebook):
    def __init__(self, *, parent, row, rowspan=1, column):
        super().__init__(parent)
        self.tab_txt = tk.Frame(self)
        self.tab_csv = tk.Frame(self)
        self.add(self.tab_txt, text='txt')
        self.add(self.tab_csv, text='csv')
        self.grid(row=row, rowspan=rowspan, column=column)
        create_notepad(self.tab_txt)
        treeview = Treeview(parent=self.tab_csv, height=10)


    # def data_table(self):


