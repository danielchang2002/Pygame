from piece import Piece
from random import random
class Board():
    def __init__(self, size):
        self.size = size
        self.setBoard()

    def setBoard(self):
        self.addToBoard()
        self.setNeighbors()
        
    def addToBoard(self):
        self.board = []
        for row in range(self.size[0]):
            row = []
            for col in range(self.size[1]):
                alive = random() > 0.5
                piece = Piece(alive)
                row.append(piece)
            self.board.append(row)
    
    def setNeighbors(self):
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                neighbors = self.getNeighborsList(row, col)
                self.board[row][col].setNeighbors(neighbors)

    def getNeighborsList(self, row, col):
        neighbors = []
        for r in range(row - 1 if row > 0 else row, row + 1 if row < self.size[0] - 1 else row):
            for c in range(col - 1 if col > 0 else col, col + 1 if col < self.size[1] - 1 else col):
                if (r == row and c == col):
                    continue
                neighbors.append(self.board[r][c])
        return neighbors

    def getBoard(self):
        return self.board

    def update(self):
        nextValues = []
        for row in self.board:
            r = []
            for piece in row:
                alive = False
                numAlive = piece.getNumAroundAlive()
                if piece.getAlive():
                    alive = numAlive >= 2 and numAlive <= 3
                else:
                    alive = numAlive == 3
                r.append(alive)
            nextValues.append(r)
        self.setValues(nextValues)

    def setValues(self, nextValues):
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                self.board[row][col].setAlive(nextValues[row][col])