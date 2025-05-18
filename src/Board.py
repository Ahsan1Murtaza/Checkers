import tkinter as tk

from config import *

class Board:
    def __init__(self, master):
        self.master = master

        # Create canvas
        self.canvas = tk.Canvas(master, width=COLUMNS * TILE_SIZE, height=ROWS * TILE_SIZE)
        self.canvas.pack()
    
        # Draw board
        self.drawBoard()



    def drawBoard(self):
        for row in range(ROWS):
            for col in range(COLUMNS):
                x1 = row * TILE_SIZE
                y1 = col * TILE_SIZE
                x2 = x1 + TILE_SIZE
                y2 = y1 + TILE_SIZE
                if (row + col) % 2 == 0:
                    color = LIGHT_COLOR
                else:
                    color = DARK_COLOR

                self.canvas.create_rectangle(x1,y1,x2,y2, fill = color)
            
    

    def onclick(self, event):
        x = event.x
        y = event.y
        row = int(y / TILE_SIZE)
        col = int(x / TILE_SIZE)
        print(f"Clicked at: ({x}, {y})")
        print(f"Clicked on Row: {row}, Col: {col}")

      