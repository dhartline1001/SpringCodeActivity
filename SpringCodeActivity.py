import tkinter as tk
from tkinter import messagebox
import random

class WhackABunnyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Whack-a-Bunny!")
        self.score = 0
        self.time_left = 30
        self.running = False
        self.active_index = -1

        self.pastel_colors = [
            "#", "#", "#",
            "#", "#", "#",
            "#", "#", "#"
        ]

        # Main container
        self.main_frame = tk.Frame(root)
        self.main_frame.pack()

        self.create_main_menu()

    def create_main_menu(self):
        # Clear the frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        title = 
        title.pack(pady=20)

        start_btn = 
        start_btn.pack(pady=10)

    def start_game(self):
        self.score = 0
        self.time_left = 30
        self.running = True

        # Clear main frame and build game UI
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        self.score_label = 
        self.score_label.pack()

        self.time_label = 
        self.time_label.pack()

        self.grid_frame = 
        self.grid_frame.pack()

        self.canvas_grid = []
        for i in range(3):
            for j in range(3):
                index = i * 3 + j
                canvas = tk.Canvas(self.grid_frame, width=100, height=100, bg=self.pastel_colors[index], highlightthickness=0)
                canvas.grid(row=i, column=j, padx=5, pady=5)
                canvas.bind("<Button-1>", lambda e, idx=index: self.hit_bunny(idx))
                text_id = canvas.create_text(50, 50, text="", font=("Arial", 36))
                self.canvas_grid.append((canvas, text_id))

        self.spawn_bunny()
        self.update_timer()

    def spawn_bunny(self):
        if not self.running:
            return
        # Clear all
        for idx, (canvas, text_id) in enumerate(self.canvas_grid):
            canvas.itemconfig(text_id, text="")
            canvas.config(bg=self.pastel_colors[idx])
        self.active_index = random.randint(0, 8)
        canvas, text_id = self.canvas_grid[self.active_index]
        canvas.itemconfig(text_id, text="🐰")
        canvas.config(bg="#90EE90")  # Highlight

        self.root.after(1000, self.spawn_bunny)

    def hit_bunny(self, index):

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.time_label.config(text=f"Time: {self.time_left}")
            self.root.after(1000, self.update_timer)
        else:
            self.running = False
            self.end_game()

    def end_game(self):


# Launch the game
if __name__ == "__main__":

