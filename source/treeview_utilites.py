import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinterdnd2 import DND_FILES, TkinterDnD
from pathlib import Path
import numpy as np
from source.Figure import *


class Treeview(ttk.Treeview):
    def __init__(self, *,
                 parent,
                 row: int = 0,
                 column: int = 0,
                 rowspan: int = 1,
                 columns: set = ('parameter', 'value'),
                 height: int = 10,
                 sticky: str = "nsew"):
        super().__init__(
            parent,
            columns=columns,
            show='headings',
            height=height,
            selectmode='browse')
        self._parent = parent
        self.heading('parameter', text='Параметр')
        self.heading('value', text='Значение')
        self.data = []
        self.bind('<Double-Button-1>', self.select_item)
        self.configure(selectmode='browse')
        self.init_data()
        self.add_scrollbar(parent, row, column, rowspan)
        # self.add_horiz_scrollbar(parent, row, column, rowspan)
        self.stored_dataframe = pd.DataFrame()
        # df = pd.read_excel('data.xlsx')
        df = pd.read_excel('result.xlsx')
        self.set_datatable(df)
        self.drop_target_register(DND_FILES)
        self.dnd_bind("<<Drop>>", self.drop_in_table)
        self.grid(row=row, rowspan=rowspan, column=column, sticky=sticky)
        self.add_export_buttons()
        # self.dnd_bind("<<Drop>>", self.drop_in_table)

    def detect(self, event):
        print('registered')

    def add_scrollbar(self, parent, row, column, rowspan):
        scrollbar = ttk.Scrollbar(parent, orient=tk.VERTICAL, command=self.yview)
        self.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=row, rowspan=rowspan, column=column + 1, sticky='ns')
        scrollbar2 = ttk.Scrollbar(parent, orient=tk.HORIZONTAL, command=self.xview)
        self.configure(xscroll=scrollbar.set)
        scrollbar2.grid(row=row + rowspan, column=column, sticky='we')

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

        # df_rows = dataframe.tolist()
        for index, row in dataframe.iterrows():
            self.insert("", "end", values=row.values.tolist())
        return None

    def pop_up_value(self, item):
        win = tk.Toplevel()
        win.wm_title("Window")
        win.geometry('500x500')
        frame = tk.Frame(win)
        text = tk.Label(frame, text=f'{item[0]}: {item[1]}')
        text.pack()
        frame.grid(row=0, column=0)
        b = ttk.Button(win, text="close", command=win.destroy)

    def pop_up_export(self, item, filename):
        win = tk.Toplevel()
        win.wm_title("Window")
        # win.geometry('500x500')
        frame = tk.Frame(win)
        text = tk.Label(frame, text=f'{item[0]} \n {item[1]}\n\n saved to: {filename}')
        text.pack()
        frame.grid(row=0, column=0)
        b = ttk.Button(win, text="close", command=win.destroy)
        exit_button = tk.Button(win, text='exit', command=win.destroy)
        exit_button.grid(row=1, column=0, sticky='nsew')

    def select_item(self, *args):
        cur_item = self.focus()
        self.pop_up_value(self.item(cur_item)['values'])

    def _parse_drop_files(self, filename):
        # 'C:/Users/Owner/Downloads/RandomStock Tickers.csv C:/Users/Owner/Downloads/RandomStockTickers.csv'
        size = len(filename)
        print(f'_parse_drop_files: {filename}')
        return filename

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

    def export(self):
        df = self.stored_dataframe
        time_up = 0
        time_down = 0
        velocity_sum_up = 0
        velocity_sum_down = 0
        counter_up = 0
        counter_down = 0
        df['ВремяГТИ'] = pd.to_datetime(df['ВремяГТИ'])

        velos_up = []
        velos_down = []
        velocity = [0] * df.shape[0]
        time_up = []
        time_down = []

        for i in range(1, df.shape[0]):
            delta = df['Блок, м'][i] - df['Блок, м'][i - 1]
            delta_time = (df['ВремяГТИ'][i] - df['ВремяГТИ'][i - 1]).total_seconds()
            if delta < -0.2:
                velos_down.append(np.abs(delta / 5))
                time_down.append(delta_time)
            elif delta > 0.21:
                velos_up.append(np.abs(delta / 5))
                time_up.append(delta_time)
            velocity[i] = delta / delta_time

        avg_up = sum(velos_up) / len(velos_up)
        avg_down = sum(velos_down) / len(velos_down)
        df['velocity'] = velocity
        filename = 'result.xlsx'
        message1 = f'средняя скорость спуска: {avg_down}'
        message2 = f'средняя скорость подъема: {np.abs(avg_up)}'
        self.pop_up_export([message1, message2], filename)
        data = {'Средняя скорость спуска': [avg_down], 'Средняя скорость подъема': [avg_up]}
        dataset = pd.DataFrame(data=data)
        dataset.to_excel(filename, index=False)

    def plot1(self):
        win = tk.Toplevel()
        win.wm_title("Глубина от среднего веса на трубе")
        # win.geometry('800x800')
        fig = Plot(parent=win, row=0, column=0)
        weights_down, deeps_down, weights_up, deeps_up = self._get_weights_deeps()
        fig.plot_task_1(weights_down, deeps_down, weights_up, deeps_up)

    def plot2(self):
        win = tk.Toplevel()
        win.wm_title("Вес и глубина от времени")
        # win.geometry('800x800')
        fig = Plot(parent=win, row=0, column=0)
        fig.plot_task_2(self.stored_dataframe['ВремяГТИ'], self.stored_dataframe['Глубина БК'],self.stored_dataframe['Вес, т'])

    def _get_weights_deeps(self):
        df = self.stored_dataframe
        diff = [0] * df.shape[0]
        for i in range(1, df.shape[0]):
            diff[i] = df['Блок, м'][i] - df['Блок, м'][i - 1]

        df['diff'] = diff

        df_up = df[df['diff'] > 0]
        df_down = df[df['diff'] < 0]
        _df_up = df_up.groupby('Глубина БК')[['Вес, т']].mean()

        count = 0
        sum_deep = 0
        deeps_up = [0]
        weights_up = [0]
        sum_weight = 0
        average_by = 15
        for i in _df_up.index:
            if _df_up['Вес, т'][i] > weights_up[-1] * 0.8:
                #         print((_df_up['Вес, т'][i]-weights_up[-1]))
                if count <= average_by - 1:
                    count += 1
                    sum_weight += _df_up['Вес, т'][i]
                    sum_deep += i
                else:
                    weights_up.append(sum_weight / average_by)
                    deeps_up.append(sum_deep / average_by)
                    count = 0
                    sum_weight = 0
                    sum_deep = 0

        _df_down = df_down.groupby('Глубина БК')[['Вес, т']].mean()
        count = 0
        sum_deep = 0
        deeps_down = [0]
        weights_down = [0]
        sum_weight = 0

        for i in _df_down.index:
            if _df_down['Вес, т'][i] > weights_down[-1] * 0.9:
                if count <= average_by - 1:
                    count += 1
                    sum_weight += _df_down['Вес, т'][i]
                    sum_deep += i
                else:
                    weights_down.append(sum_weight / average_by)
                    deeps_down.append(sum_deep / average_by)
                    count = 0
                    sum_weight = 0
                    sum_deep = 0
        return weights_down, deeps_down, weights_up, deeps_up

    def add_export_buttons(self):
        parent = self._parent
        button_frame = tk.Frame(parent)
        button_frame.grid(row=2, column=0, sticky='w')
        button_export = tk.Button(button_frame, text='Export', command=self.export)
        button_export.grid(row=0, column=0, sticky='w')

        button_plot1 = tk.Button(button_frame, text='Глубина от веса', command=self.plot1)
        button_plot1.grid(row=0, column=1, sticky='w')

        button_plot2 = tk.Button(button_frame, text='Вес и положение от времени', command=self.plot2)
        button_plot2.grid(row=0, column=2, sticky='w')
