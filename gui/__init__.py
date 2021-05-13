from tkinter import *

import numpy as np
from PIL import ImageGrab, ImageOps

from .stats import Stats
from .utils import predict


class App(Tk):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.x, self.y = 0, 0

        # Initialize the GUI with title, and the sizing
        self.title("MNIST Digit Recognizer")
        self.geometry("650x500")

        # Configure column and rows
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Configure Main canvas
        size = 250

        self.canvas = Canvas(self, height=size, width=size, bg="white")
        self.canvas.place(x=10, y=10)

        # Configure buttons
        self.clear_btn = Button(
            self, text="Clear", height=2, width=10, command=self.clear
        )
        self.clear_btn.place(x=20, y=265)

        self.predict_btn = Button(
            self, text="Predict", height=2, width=10, command=self.predict
        )
        self.predict_btn.place(x=130, y=265)

        # Prediction label and bars representation
        self.prediction = Label(
            self,
            width=20,
            height=2,
            text="Predict to get result.",
            font="Helvetica 14 bold",
        )
        self.prediction.place(x=280, y=100)

        self.bars = Stats(self)
        self.bars.init()

    def click(self, event) -> None:
        """On Click event response."""
        self.x = event.x
        self.y = event.y

    def draw(self, event) -> None:
        """Event to handle the drawing of Digit."""
        self.canvas.create_rectangle(
            (self.x, self.y, event.x, event.y), fill="black", width=11
        )
        self.x = event.x
        self.y = event.y

    def clear(self) -> None:
        """Function to clear up the canvas, when clear button is clicked."""
        self.canvas.delete("all")
        self.prediction.configure(text="Predict to get result.")
        self.bars.clear()

    def predict(self) -> None:
        """Predict the digit drawn on the canvas."""
        # Update the canvar
        self.canvas.update()

        # Get the X and Y dimensions
        x = self.winfo_rootx() + self.canvas.winfo_x()
        y = self.winfo_rooty() + self.canvas.winfo_y()

        # Get the new dimensions by adding previous ones to the widget info
        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()

        # Grab the image, and save it to buffer
        image = ImageGrab.grab().crop((x, y, x1, y1))
        image = ImageOps.invert(image)
        image = np.array(image.resize((28, 28)).convert("L"))

        # Predict and get scores
        prediction, pred_array = predict(image)

        # Display the scores
        self.prediction.configure(text=f"Prediction : {prediction}")
        self.bars.show(pred_array)

    def start(self) -> None:
        self.canvas.bind("<Button-1>", self.click)
        self.canvas.bind("<B1-Motion>", self.draw)

        self.mainloop()
