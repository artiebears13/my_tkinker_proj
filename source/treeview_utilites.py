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
        self.bind('<Double-Button-1>', self.select_item)

        self.init_data()
        self.add_scrollbar(parent, row, column, rowspan)
        self.stored_dataframe = pd.DataFrame()
        # self.file_names_listbox.place(relheight=1, relwidth=0.25)
        # self.file_names_listbox = tk.Listbox(parent, selectmode=tk.SINGLE, background="darkgray")
        # self.file_names_listbox.place(relheight=0.1, relwidth=0.25)
        # self.file_names_listbox.drop_target_register(DND_FILES)
        # self.file_names_listbox.dnd_bind("<<Drop>>", self.detect)
        # self.file_names_listbox.bind("<Double-1>", self.detect)
        self.drop_target_register(DND_FILES)
        self.dnd_bind("<<Drop>>", self.detect)
        self.grid(row=row, rowspan=rowspan, column=column, sticky='wsew')
        # self.dnd_bind("<<Drop>>", self.drop_in_table)

    def detect(self, event):
        print('registered')

    def add_scrollbar(self, parent, row, column, rowspan):
        scrollbar = ttk.Scrollbar(parent, orient=tk.VERTICAL, command=self.yview)
        self.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=row, rowspan=rowspan, column=column + 1, sticky='ns')

    def init_data(self):
        for i in range(1, 100):
            self.data.append((f'параметр {i}', i))
        for data in self.data:
            self.insert('', 'end', values=data)

    def set_datatable(self, dataframe):
        self.stored_dataframe = dataframe
        self._draw_table(dataframe)

    def _draw_table(self, dataframe):
        self.delete(*self.get_children())
        columns = list(dataframe.columns)
        self.__setitem__("column", columns)
        self.__setitem__("show", "headings")

        for col in columns:
            self.heading(col, text=col)

        df_rows = dataframe.tolist()
        for row in df_rows:
            self.insert("", "end", values=row)
        return None

    def pop_up_value(self, item):
        win = tk.Toplevel()
        win.wm_title("Window")
        win.geometry('500x500')
        frame = tk.Frame(win)
        text = tk.Label(frame, text=f'{item[0]} = {item[1]}')
        text.pack()
        frame.grid(row=0, column=0)
        b = ttk.Button(win, text="close", command=win.destroy)

    def select_item(self, *args):
        cur_item = self.focus()
        self.pop_up_value(self.item(cur_item)['values'])

    def _parse_drop_files(self, filename):
        # 'C:/Users/Owner/Downloads/RandomStock Tickers.csv C:/Users/Owner/Downloads/RandomStockTickers.csv'
        size = len(filename)
        print(f'_parse_drop_files: {filename}')
        res = []  # list of file paths
        name = ""
        idx = 0
        while idx < size:
            if filename[idx] == "{":
                j = idx + 1
                while filename[j] != "}":
                    name += filename[j]
                    j += 1
                res.append(name)
                name = ""
                idx = j
            elif filename[idx] == " " and name != "":
                res.append(name)
                name = ""
            elif filename[idx] != " ":
                name += filename[idx]
            idx += 1
        if name != "":
            res.append(name)
        return res

    def drop_in_table(self, event):
        file_path = self._parse_drop_files(event.data)
        print('drop')
        if file_path.endswith(".csv"):
            # path_object = Path(file_path)
            # file_name = path_object.name
            df = pd.read_csv(file_path)
            self.set_datatable(dataframe=df)
            # if file_name not in current_listbox_items:
            #     self.file_names_listbox.insert("end", file_name)
            #     self.path_map[file_name] = file_path
