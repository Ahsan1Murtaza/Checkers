# main.py

import tkinter as tk
from Board import Board

if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)
    root.title("Checkers Game")

    board = Board(root)
    board.canvas.bind("<Button-1>", board.onclick)

    root.mainloop()
