from tkinter import *


class App(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.x, self.y = 0, 0

        self.title("MNIST Digit Recognizer")
        self.geometry("700x600")

        # Configure column and rows
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Configure canvas
        self.canvas = Canvas(self, height=200, width=200, bg="white")
        self.canvas.place(x=10, y=10)

        # Configure buttons
        self.clear_btn = Button(self, text="Clear", height=2, width=15, command=self.clear)
        self.clear_btn.place(x=215, y=15)

        self.predict_btn = Button(self, text="Predict", height=2, width=15)
        self.predict_btn.place(x=215, y=75)

    def click(self, event):
        self.x = event.x
        self.y = event.y

    def draw(self, event):
        self.canvas.create_rectangle((self.x, self.y, event.x, event.y), fill="black", width=10)
        self.x = event.x
        self.y = event.y

    def clear(self):
        self.canvas.delete("all")

    def start(self):
        self.canvas.bind("<Button-1>", self.click)
        self.canvas.bind("<B1-Motion>", self.draw)

        self.mainloop()
