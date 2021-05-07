import os
from tkinter import *

import cv2
from PIL import ImageGrab, ImageOps

from .stats import Stats
from .utils import predict


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
        size = 200

        self.canvas = Canvas(self, height=size, width=size, bg="white")
        self.canvas.place(x=10, y=10)

        self.image = Canvas(self, height=30, width=30, bg="white")

        # Configure buttons
        self.clear_btn = Button(self, text="Clear", height=2, width=15, command=self.clear)
        self.clear_btn.place(x=215, y=15)

        self.predict_btn = Button(self, text="Predict", height=2, width=15, command=self.predict)
        self.predict_btn.place(x=215, y=75)

        # Prediction
        self.prediction = Label(self, width=20, height=2, text="Predict to get result.")
        self.prediction.place(x=100, y=250)

        self.bars = Stats(self)
        self.bars.init()

    def click(self, event):
        self.x = event.x
        self.y = event.y

    def draw(self, event):
        self.canvas.create_rectangle((self.x, self.y, event.x, event.y), fill="black", width=10)
        self.x = event.x
        self.y = event.y

    def clear(self):
        self.canvas.delete("all")
        self.prediction.configure(text="Predict to get result.")
        self.bars.clear()

    def predict(self):
        filename = "digit.png"

        x = self.winfo_rootx() + self.canvas.winfo_x()
        y = self.winfo_rooty() + self.canvas.winfo_y()

        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()

        # Grab the image, and save it.
        image = ImageGrab.grab().crop((x, y, x1, y1))
        image = ImageOps.invert(image.resize((28, 28)))
        image.save(filename)

        # Read and process the image.
        image = cv2.imread(filename, cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Predict and get scores
        prediction, pred_array = predict(gray)

        # Display the image
        digit = PhotoImage(file=filename)
        self.image.create_image(220, 220, image=digit, anchor=NW)

        self.prediction.configure(text=f"Prediction : {prediction}")
        self.bars.show(pred_array)

        try:
            os.remove(filename)
        except Exception:
            pass

    def start(self):
        self.canvas.bind("<Button-1>", self.click)
        self.canvas.bind("<B1-Motion>", self.draw)

        self.mainloop()
