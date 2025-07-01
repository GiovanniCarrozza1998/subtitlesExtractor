import tkinter as tk


class RegionSelector(tk.Tk):
    """
    A Tkinter-based class to allow the user to select a screen region.
    This region will be captured in screenshots.
    """

    def __init__(self):
        super().__init__()
        self.left = None
        self.right = None
        self.top = None
        self.bottom = None
        self.attributes('-alpha', 0.3)  # Make the window partially transparent
        self.attributes("-fullscreen", True)
        self.attributes("-topmost", True)
        self.canvas = tk.Canvas(self, cursor="cross", bg="grey")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.rect = None
        self.start_x = self.start_y = None
        self.end_x = self.end_y = None
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def on_press(self, event):
        """Handles the mouse button press event for starting the selection rectangle."""
        self.start_x = self.winfo_pointerx()
        self.start_y = self.winfo_pointery()
        if self.rect:
            self.canvas.delete(self.rect)
        self.rect = self.canvas.create_rectangle(
            self.start_x, self.start_y, self.start_x, self.start_y,
            outline='red', width=2
        )

    def on_drag(self, event):
        """Updates the selection rectangle as the mouse is dragged."""
        cur_x = self.winfo_pointerx()
        cur_y = self.winfo_pointery()
        self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)

    def on_release(self, event):
        """Finalizes the selection region when the mouse button is released."""
        self.end_x = self.winfo_pointerx()
        self.end_y = self.winfo_pointery()
        self.set_region()
        self.destroy()

    def set_region(self):
        """Calculates the region coordinates from the selected area."""
        x1, y1, x2, y2 = self.start_x, self.start_y, self.end_x, self.end_y
        self.left, self.right = min(x1, x2), max(x1, x2)
        self.top, self.bottom = min(y1, y2), max(y1, y2)
        print("Coordinates of the selected vertices:")
        print(f"Top left: ({self.left}, {self.top})")
        print(f"Bottom right: ({self.right}, {self.bottom})")

    def get_region(self):
        """Returns the coordinates of the selected region."""
        return self.left, self.right, self.top, self.bottom