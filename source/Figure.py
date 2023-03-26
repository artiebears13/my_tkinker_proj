import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np


class Plot(tk.Frame):
    def __init__(self, *,
                 parent: tk.Tk,
                 row: int,
                 column: int,
                 sticky: str = 'nsew'):
        super().__init__(parent)
        self.configure(bg='white')
        self.grid(row=row, column=column, sticky=sticky)

    def add_plot(self):
        fig = Figure(figsize=(2, 2),
                     dpi=100)

        # list of squares
        y = [i ** 2 for i in range(101)]
        # fig.show()
        plot1 = fig.add_subplot(111)

        # plotting the graph
        plot1.plot(y)

        # creating the Tkinter canvas
        # containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()

        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().pack()

        # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()

        # placing the toolbar on the Tkinter window
        canvas.get_tk_widget().pack()

    def plot_task_1(self, weights_down, deeps_down, weights_up, deeps_up):
        fig = Figure(
            dpi=100)
        plot1 = fig.add_subplot(121)
        z = np.polyfit(weights_down, deeps_down, 3)
        p = np.poly1d(z)
        plot1.scatter(weights_down, deeps_down, color='red', label='вниз', s=10)
        plot1.plot(weights_down, p(weights_down), "r--", label='trend вниз')
        plot1.legend()

        plot2 = fig.add_subplot(122)
        z = np.polyfit(weights_up, deeps_up, 3)
        p = np.poly1d(z)

        plot2.plot(weights_up, p(weights_up), "b--", label='trend вверх')
        plot2.scatter(weights_up, deeps_up, color='blue', label='вверх', s=15)
        plot2.legend()
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()

        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().pack()

        # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()

        # placing the toolbar on the Tkinter window
        canvas.get_tk_widget().pack()

    def plot_task_2(self, x,y1, y2):
        fig = Figure(figsize=(10, 5),
                     dpi=100)

        plot1 = fig.add_subplot(121)
        plot1.scatter(x,y1, s=5)
        plot1.set_xlabel('Время')
        plot1.set_ylabel('Вес')
        plot1.set_title('Вес блока от времени')

        plot2 = fig.add_subplot(122)
        plot2.scatter(x, y2, s=5)
        plot2.set_xlabel('Время')
        plot2.set_ylabel('Глубина БК')
        plot2.set_title('Глубина от времени')

        # plot1.title('Вес блока от времени')

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()

        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().pack()

        # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()

        # placing the toolbar on the Tkinter window
        canvas.get_tk_widget().pack()
