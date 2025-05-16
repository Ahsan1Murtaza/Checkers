# main.py

import tkinter as tk
from Board import Board

if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)
    root.title("Checkers Game")

    Board(root)


    root.mainloop()
