# Програма для побудови прямокутників
import tkinter as tk
from tkinter import colorchooser


# Model
class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color


# View
class RectangleView:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack()

        self.controls_frame = tk.Frame(root)
        self.controls_frame.pack()

        self.x_label = tk.Label(self.controls_frame, text="X:")
        self.x_label.grid(row=0, column=0)
        self.x_entry = tk.Entry(self.controls_frame)
        self.x_entry.grid(row=0, column=1)

        self.y_label = tk.Label(self.controls_frame, text="Y:")
        self.y_label.grid(row=1, column=0)
        self.y_entry = tk.Entry(self.controls_frame)
        self.y_entry.grid(row=1, column=1)

        self.width_label = tk.Label(self.controls_frame, text="Width:")
        self.width_label.grid(row=2, column=0)
        self.width_entry = tk.Entry(self.controls_frame)
        self.width_entry.grid(row=2, column=1)

        self.height_label = tk.Label(self.controls_frame, text="Height:")
        self.height_label.grid(row=3, column=0)
        self.height_entry = tk.Entry(self.controls_frame)
        self.height_entry.grid(row=3, column=1)

        self.color_label = tk.Label(self.controls_frame, text="Color:")
        self.color_label.grid(row=4, column=0)
        self.color_button = tk.Button(self.controls_frame, text="Choose", command=self.choose_color)
        self.color_button.grid(row=4, column=1)

        self.add_button = tk.Button(self.controls_frame, text="Add Rectangle", command=None)
        self.add_button.grid(row=5, column=0, columnspan=2)

        self.selected_color = "#000000"

    def choose_color(self):
        color_code = colorchooser.askcolor(title="Choose Color")[1]
        if color_code:
            self.selected_color = color_code

    def draw_rectangle(self, rectangle):
        self.canvas.create_rectangle(
            rectangle.x, rectangle.y,
            rectangle.x + rectangle.width,
            rectangle.y + rectangle.height,
            fill=rectangle.color, outline="black"
        )


# Controller
class RectangleController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.add_button.config(command=self.add_rectangle)

    def add_rectangle(self):
        try:
            x = int(self.view.x_entry.get())
            y = int(self.view.y_entry.get())
            width = int(self.view.width_entry.get())
            height = int(self.view.height_entry.get())
            color = self.view.selected_color

            rectangle = Rectangle(x, y, width, height, color)
            self.model.append(rectangle)
            self.view.draw_rectangle(rectangle)
        except ValueError:
            print("Invalid input. Please enter numeric values for x, y, width, and height.")


# Main
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Rectangle Drawer")

    model = []
    view = RectangleView(root)
    controller = RectangleController(model, view)

    root.mainloop()
