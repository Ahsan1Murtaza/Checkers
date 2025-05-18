import tkinter as tk

from config import *
from Piece import Piece

class Board:
    def __init__(self, master):
        self.master = master

        # Initialize board
        self.board = [[None for _ in range(COLUMNS)] for _ in range(ROWS)]
        # Create canvas
        self.canvas = tk.Canvas(master, width=COLUMNS * TILE_SIZE, height=ROWS * TILE_SIZE)
        self.canvas.pack()
    
        self.canvas.bind("<Button-1>", self.onclick)

        # Draw board
        self.drawBoard()

        # Initialize Board List
        self.initializeBoard()

        # Draw pieces
        self.drawPieces()


    def drawBoard(self):
        for row in range(ROWS):
            for col in range(COLUMNS):
                x1 = col * TILE_SIZE
                y1 = row * TILE_SIZE
                x2 = x1 + TILE_SIZE
                y2 = y1 + TILE_SIZE
                if (row + col) % 2 == 0:
                    color = LIGHT_COLOR
                else:
                    color = DARK_COLOR

                self.canvas.create_rectangle(x1,y1,x2,y2, fill = color)

    def initializeBoard(self): # Internal method to set up the board
        # Black Pieces
        self.board[0][1] = Piece("BLACK")
        self.board[0][3] = Piece("BLACK")
        self.board[0][5] = Piece("BLACK")
        self.board[0][7] = Piece("BLACK")

        self.board[1][0] = Piece("BLACK")
        self.board[1][2] = Piece("BLACK")
        self.board[1][4] = Piece("BLACK")
        self.board[1][6] = Piece("BLACK")

        self.board[2][1] = Piece("BLACK")
        self.board[2][3] = Piece("BLACK")
        self.board[2][5] = Piece("BLACK")
        self.board[2][7] = Piece("BLACK")

        # White Pieces
        self.board[5][0] = Piece("WHITE")
        self.board[5][2] = Piece("WHITE")
        self.board[5][4] = Piece("WHITE")
        self.board[5][6] = Piece("WHITE")

        self.board[6][1] = Piece("WHITE")
        self.board[6][3] = Piece("WHITE")
        self.board[6][5] = Piece("WHITE")
        self.board[6][7] = Piece("WHITE")

        self.board[7][0] = Piece("WHITE")
        self.board[7][2] = Piece("WHITE")
        self.board[7][4] = Piece("WHITE")
        self.board[7][6] = Piece("WHITE")
            

    def drawPieces(self): # Drawing pieces on the board using board list
        for row in range(ROWS):
            for col in range(COLUMNS):
                piece = self.board[row][col]
                if piece is not None:
                    x1 = col * TILE_SIZE
                    y1 = row * TILE_SIZE
                    x2 = x1 + TILE_SIZE
                    y2 = y1 + TILE_SIZE
                    color = piece.color
                    if color == "BLACK":
                        self.canvas.create_oval(x1, y1, x2, y2, fill="Black")
                    elif color == "WHITE":
                        self.canvas.create_oval(x1, y1, x2, y2, fill="White")


    def onclick(self, event):
        x = event.x
        y = event.y
        row = int(y / TILE_SIZE)
        col = int(x / TILE_SIZE)
        # print(f"Clicked at: ({x}, {y})")
        # print(f"Clicked on Row: {row}, Col: {col}")
        if self.board[row][col] is not None:
            print(f"Piece at ({row}, {col}) is {self.board[row][col].color}")
        else:
            print(f"No piece at ({row}, {col})")

    

      