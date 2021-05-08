from tkinter import *
from tkinter.ttk import *


class Stats:
    def __init__(self, gui):
        self.gui = gui

        self.bars, self.labels = [None] * 10, [None] * 10

    def init(self):
        for i in range(10):
            self.labels[i] = LabelFrame(self.gui, text=str(i))
            self.bars[i] = Progressbar(
                self.labels[i], orient=HORIZONTAL, length=100, mode='determinate', value=1, maximum=100
            )

        self.labels[0].place(x=500, y=0, height=30, width=130)
        self.bars[0].place(x=7, y=-2)

        for i in range(1, 10):
            self.labels[i].place(x=500, y=30*i, height=30, width=130)
            self.bars[i].place(x=7, y=-2)

    def clear(self):
        for i in range(10):
            self.bars[i]['value'] = 1
        self.gui.update()

    def show(self, stats):
        for i in range(10):
            amount = stats[0][i]
            self.bars[i]['value'] = amount * 1000

        self.gui.update()
