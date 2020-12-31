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
                alive = random() < 0
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
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if (c < 0 or c >= self.size[1] or r < 0 or r >= self.size[0]):
                    continue
                if (r == row and c == col):
                    continue
                neighbors.append(self.board[r][c])
        return neighbors

    def getBoard(self):
        return self.board

    def update(self):
        nextValues = []
        for row in range(self.size[0]):
            r = []
            for col in range(self.size[1]):
                piece = self.board[row][col]
                alive = False
                numAlive = piece.getNumAroundAlive()
                if piece.getAlive():
                    alive = numAlive == 2 or numAlive == 3
                else:
                    alive = numAlive == 3
                r.append(alive)
            nextValues.append(r)
        self.setValues(nextValues)

    def setValues(self, nextValues):
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                self.board[row][col].setAlive(nextValues[row][col])
    
    def handleClick(self, position):
        self.board[position[0]][position[1]].toggle()