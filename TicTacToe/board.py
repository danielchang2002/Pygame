from copy import deepcopy

class Board():
    def __init__(self, board):
        if (not board):
            self.board = []
            for i in range(3):
                row = []
                for j in range(3):
                    row.append('-')
                self.board.append(row)
        else:
            self.board = board
    
    def getPiece(self, index):
        return self.board[index[0]][index[1]]
    
    def getMovedBoard(self, index, player):
        newBoard = self.board
        newBoard[index[0]][index[1]] = player
        return Board(newBoard)
    
    def getHasWon(self, player):
        for row in range(3):
            won = True
            for col in range(0, 3):
                if (self.getPiece((row, col)) != player):
                    won = False
                    break
            if (won):
                return ((row, 0), (row, 1), (row, 2))
        for col in range(3):
            won = True
            for row in range(0, 3):
                if (self.getPiece((row, col)) != player):
                    won = False
                    break
            if (won):
                return ((0, col), (1, col), (2, col))
        if (self.getPiece((0, 0)) == player and self.getPiece((1, 1)) == player and self.getPiece((2, 2)) == player): 
            return ((0, 0), (1, 1), (2, 2))
        elif (self.getPiece((0, 2)) == player and self.getPiece((1, 1)) == player and self.getPiece((2, 0)) == player):
            return ((0, 2), (1, 1), (2, 0))

    def isFull(self):
        num = 0
        for i in range(3):
            for j in range(3):
                if (self.board[i][j] != '-'):
                    num += 1
        return num == 9
    
    def getNeighbors(self, player):
        neighbors = []
        for i in range(3):
            for j in range(3):
                if self.getPiece((i, j)) == '-':
                    board = deepcopy(self.board)
                    board[i][j] = player
                    neighbors.append(Board(board))
        return neighbors
