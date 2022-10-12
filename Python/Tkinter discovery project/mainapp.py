import tkinter as tk
from tkinter import *

class mainWindow:
    def __init__(self, win_X, win_Y) -> None:
        self.win_X = str(win_X)
        self.win_Y = str(win_Y)
        self.ttk = tk.Tk()
        self.ttk.geometry(win_X, win_Y)
        self.ttk.minsize(win_X - 100, win_Y - 100)
        self.ttk.maxsize(win_X + 300, win_Y + 300)
        self.ttk.title("Home page")
        self.ttk['bg'] = "#23262e"


if __name__ == "__main__":
    mainWindow(920, 640)