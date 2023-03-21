import tkinter as tk


class UserData(tk.Frame):
    def __init__(self, *,
                 parent: tk.Tk,
                 row: int,
                 column: int,
                 sticky: str = 'nsew'):
        super().__init__(parent)
        self.configure(bg='white')
        self.grid(row=row, column=column, sticky=sticky)

    def add_insert_frame(self,
                         command: (),
                         row: int,
                         column: int,
                         sticky: str = 'nsew',
                         label_text: str = 'label',
                         button_text: str = 'ok',
                         ):
        frame = tk.Frame(self)
        frame.configure(bg='white', background='white')
        label = tk.Label(frame, text=label_text, bg='white')
        entry = tk.Entry(frame, bg='white')
        entry.bind('<Return>', func=lambda action: command(label_text, entry.get()))
        button = tk.Button(frame, text=button_text, bg='white', background='white')
        button.configure(command=lambda: command(label_text, entry.get()))
        label.pack(side='left')
        button.pack(side='right')
        entry.pack(side='right')

        frame.grid(row=row, column=column, sticky=sticky)
