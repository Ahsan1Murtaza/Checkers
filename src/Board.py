# import sys
import tkinter as tk

from config import *
from Piece import Piece

class Board:
    def __init__(self, master):
        self.master = master
        
        self.turn = True # True for White, False for Black

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

        self.possibleMoves = [[0 for col in range(COLUMNS)] for row in range(ROWS)]


    def switchTurn(self):
        self.turn = not(self.turn)

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
                        if (piece.king):
                            self.canvas.create_oval(x1, y1, x2, y2, fill="RED")
                            continue
                        self.canvas.create_oval(x1, y1, x2, y2, fill="Black")
                    elif color == "WHITE":
                        if (piece.king):
                            self.canvas.create_oval(x1, y1, x2, y2, fill="Orange")
                            continue
                        self.canvas.create_oval(x1, y1, x2, y2, fill="White")


    def onLeftClick(self, event):

        self.possibleMoves = [[0 for col in range(COLUMNS)] for row in range(ROWS)]

        x = event.x
        y = event.y
        row = int(y / TILE_SIZE)
        col = int(x / TILE_SIZE)
        piece = self.board[row][col]
        
        if piece.color is not None:
            self.selectedPiece = piece
            self.calculatePossibleMoves(piece)
            self.canvas.delete("all")
            self.drawBoard()
            self.drawPieces()
            self.highlightMoves()
            
            print(f"Piece at ({row}, {col}) is {piece.color}") # Debugging line
      
        else:
            self.selectedPiece = None
            self.calculatePossibleMoves(piece)
            self.canvas.delete("all")
            self.drawBoard()
            self.drawPieces()
            self.highlightMoves()
            print(f"No piece at ({row}, {col})") # Debugging line

        

    def onRightClick(self, event):
        x = event.x
        y = event.y
        row = int(y / TILE_SIZE)
        col = int(x / TILE_SIZE)
        destination = self.board[row][col]

        if self.selectedPiece is None: # if a piece is selected then we can only move it 
            return
        

        if self.selectedPiece.color is not None: # if a piece is not none specifically color then we can only move it
            if (self.selectedPiece.color == "BLACK"):
                if (not(self.turn == False)):
                    print("Not Black's Turn")
                    return
            if (self.selectedPiece.color == "WHITE"):
                if (not(self.turn == True)):
                    print("Not White's Turn")
                    return
                
            if (self.isValidMove(self.selectedPiece, destination)):

                self.isValidMovement(self.selectedPiece, destination)
            
                self.movePiece(self.selectedPiece, destination)

                self.selectedPiece = None

                self.switchTurn()
            else:
                print(f"Invalid move from ({self.selectedPiece.row}, {self.selectedPiece.column}) to ({row}, {col})")
          



    def movePiece(self, piece1, destination):
        oldRow = piece1.row
        oldCol = piece1.column

        newRow = destination.row
        newCol = destination.column

        # Check if it was a jump Move so to make it's mid piece color none
        if (abs(newRow - oldRow) == 2 and abs(newCol - oldCol)):
            midRow = (oldRow + newRow) // 2
            midCol = (oldCol + newCol) // 2
            self.board[midRow][midCol] = Piece(None, midRow, midCol)

        # Updating the piece's position
        piece1.row = newRow
        piece1.column = newCol
        piece1.king = self.makeKing(piece1, destination)

        # Updating the board
        self.board[oldRow][oldCol] = Piece(None, oldRow, oldCol)
        self.board[newRow][newCol] = piece1

        self.canvas.delete("all")
        self.drawBoard()
        self.drawPieces()

        if (self.checkWin()):
            print("GAME OVER !")
            self.canvas.unbind("<Button-1>")
            self.canvas.unbind("<Button-3>")
            # sys.exit(0)


    def isValidMove(self, piece1, destination):
        
        return self.isValidMovement(piece1, destination) # it handles both one diagnal move pluss jump over opponent
    

    # Pieces can only move forward with respect to their positions
    # can only move diagnally only if there is no piece
    # if jumping over piece then in middle of its way should be the piece of opponent

    def singleMove(self, piece1, destination):
        if (piece1.color == "BLACK"):
            steps = 1
        elif (piece1.color == "WHITE"):
            steps = -1
        else:
            return

        rowChange = destination.row - piece1.row
        colChange = destination.column - piece1.column

        rowChange = rowChange * steps
        
        # Moving single step diagnally if destination is none
        if ((rowChange == 1) and (colChange == 1 or colChange == -1) and (destination.color == None)):
            return True
      
    def jumpMove(self, piece1, destination):
        if (piece1.color == "BLACK"):
            steps = 1
        elif (piece1.color == "WHITE"):
            steps = -1
        else:
            return False

        rowChange = destination.row - piece1.row
        colChange = destination.column - piece1.column
        rowChange = rowChange * steps

        # Moving two step diagnally if midPiece is opponent and destination is none
        if ((rowChange == 2) and (colChange == 2 or colChange == -2) and (destination.color == None)):
            # Finding mid column
            midColumn = (piece1.column + destination.column) // 2
            
            # Finding mid row
            midRow = (piece1.row + destination.row) // 2

            midPiece = self.board[midRow][midColumn]

            return (not(midPiece.color == None) and not(midPiece.color == piece1.color))

        return False
       

    def makeKing(self, piece1, destination):
        color = piece1.color
        
        if (color == "BLACK" and destination.row == 7):
            piece1.king = True
            print("BLACK BECOMES KING")
        elif (color == "WHITE" and destination.row == 0):
            print("WHITE BECOMES KING")
            piece1.king = True

        return piece1.king
    
    def kingMove(self, piece1, destination):

        rowChange = destination.row - piece1.row
        colChange = destination.column - piece1.column
        
        # Diagonal Single move
        if ((rowChange == 1 or rowChange == -1) and (colChange == 1 or colChange == -1) and (destination.color == None)):
            return True
        
        # Diagonal Jump Move 
        if ((rowChange == 2 or rowChange == -2) and (colChange == 2 or colChange == -2) and (destination.color == None)):
    
            # Finding mid column
            midColumn = (piece1.column + destination.column) // 2
            midRow = (piece1.row + destination.row) // 2

            midPiece = self.board[midRow][midColumn] # get the mid piece

            return (not(midPiece.color == None) and not(midPiece.color == piece1.color))

        return False


    def isValidMovement(self, piece1, destination):

        if (piece1.king):
            return self.kingMove(piece1, destination)
        
        return self.singleMove(piece1, destination) or self.jumpMove(piece1, destination)
        

    def printArray(self):
        for i in range(8):
            for j in range(8):
                print(self.board[i][j].color , " is King ", self.board[i][j].king, "Row : " , self.board[i][j].row, " Column : " , self.board[i][j].column)


    def checkWin(self):
        whiteCount = 0
        blackCount = 0
        for col in range(COLUMNS):
            for row in range(ROWS):
                piece = self.board[col][row]
                if (piece.color == "WHITE"):
                    whiteCount += 1
                    pass
                elif (piece.color == "BLACK"):
                    blackCount += 1

        if (blackCount == 0):
            print("WHITE WINS")
            return True
        elif (whiteCount == 0):
            print("BLACK WINS")
            return True
        
        return False
        
    
    def calculatePossibleMoves(self, piece):
        if (piece.color == "BLACK" and self.turn == 1) or (piece.color == "WHITE" and self.turn == 0):
            return
        for row in range(8):
            for col in range(8):
                temp = self.board[row][col]

                if (temp.color is None and self.isValidMove(piece, temp)):
                    self.possibleMoves[row][col] = 1


    def highlightMoves(self):
        for row in range(8):
            for col in range(8):
                if (self.possibleMoves[row][col] == 1):
                    x1 = col * TILE_SIZE
                    y1 = row * TILE_SIZE
                    x2 = x1 + TILE_SIZE
                    y2 = y1 + TILE_SIZE
                    self.canvas.create_oval(x1,y1,x2,y2, fill = "Yellow")
    



      