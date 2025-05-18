import tkinter as tk

from config import *
from Piece import Piece

class Board:
    def __init__(self, master):
        self.master = master

        # Creating board
        self.board = [[Piece(None, row, col) for col in range(COLUMNS)] for row in range(ROWS)]
        # Create canvas
        self.canvas = tk.Canvas(master, width=COLUMNS * TILE_SIZE, height=ROWS * TILE_SIZE)
        self.canvas.pack()
    
        self.canvas.bind("<Button-1>", self.onLeftClick)
        self.canvas.bind("<Button-3>", self.onRightClick)

        self.selectedPiece = None

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
        self.board[0][1] = Piece("BLACK", 0, 1)
        self.board[0][3] = Piece("BLACK", 0, 3)
        self.board[0][5] = Piece("BLACK", 0, 5)
        self.board[0][7] = Piece("BLACK", 0, 7)

        self.board[1][0] = Piece("BLACK", 1, 0)
        self.board[1][2] = Piece("BLACK", 1, 2)
        self.board[1][4] = Piece("BLACK", 1, 4)
        self.board[1][6] = Piece("BLACK", 1, 6)

        self.board[2][1] = Piece("BLACK", 2, 1)
        self.board[2][3] = Piece("BLACK", 2, 3)
        self.board[2][5] = Piece("BLACK", 2, 5)
        self.board[2][7] = Piece("BLACK", 2, 7)

        # White Pieces
        self.board[5][0] = Piece("WHITE", 5, 0)
        self.board[5][2] = Piece("WHITE", 5, 2)
        self.board[5][4] = Piece("WHITE", 5, 4)
        self.board[5][6] = Piece("WHITE", 5, 6)

        self.board[6][1] = Piece("WHITE", 6, 1)
        self.board[6][3] = Piece("WHITE", 6, 3)
        self.board[6][5] = Piece("WHITE", 6, 5)
        self.board[6][7] = Piece("WHITE", 6, 7)

        self.board[7][0] = Piece("WHITE", 7, 0)
        self.board[7][2] = Piece("WHITE", 7, 2)
        self.board[7][4] = Piece("WHITE", 7, 4)
        self.board[7][6] = Piece("WHITE", 7, 6)
            

    def drawPieces(self): # Drawing pieces on the board using board list
        for row in range(ROWS):
            for col in range(COLUMNS):
                piece = self.board[row][col]
                if piece.color is not None:
                    x1 = col * TILE_SIZE
                    y1 = row * TILE_SIZE
                    x2 = x1 + TILE_SIZE
                    y2 = y1 + TILE_SIZE
                    color = piece.color
                    if color == "BLACK":
                        self.canvas.create_oval(x1, y1, x2, y2, fill="Black")
                    elif color == "WHITE":
                        self.canvas.create_oval(x1, y1, x2, y2, fill="White")


    def onLeftClick(self, event):
        x = event.x
        y = event.y
        row = int(y / TILE_SIZE)
        col = int(x / TILE_SIZE)
        piece = self.board[row][col]
        
        if piece is not None:
            self.selectedPiece = piece
            print(f"Piece at ({row}, {col}) is {piece.color}") # Debugging line
        else:
            self.selectedPiece = None
            print(f"No piece at ({row}, {col})") # Debugging line

    def onRightClick(self, event):
        x = event.x
        y = event.y
        row = int(y / TILE_SIZE)
        col = int(x / TILE_SIZE)
        destination = self.board[row][col]

        if self.selectedPiece.color is not None: # if a piece is not none specifically color then we can only move it
            if (self.isValidMove(self.selectedPiece, destination)):
                self.movePiece(self.selectedPiece, destination)
                self.selectedPiece = None
          



    def movePiece(self, piece1, destination):
        oldRow = piece1.row
        oldCol = piece1.column

        newRow = destination.row
        newCol = destination.column

        print(f"Moving piece from ({oldRow}, {oldCol}) to ({newRow}, {newCol})") # Debugging line

        # Updating the piece's position
        piece1.row = newRow
        piece1.column = newCol

        # Updating the board
        self.board[oldRow][oldCol] = Piece(None, oldRow, oldCol)
        self.board[newRow][newCol] = piece1

        self.canvas.delete("all")
        self.drawBoard()
        self.drawPieces()


    def isValidMove(self, piece1, destination):
        return True

      