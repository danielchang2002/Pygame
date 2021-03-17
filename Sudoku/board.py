import csv
class Board():
    def __init__(self, size, board=None):
        self.size = size
        self.rows, self.cols = self.size
        self.setBoard()
        if board:
            with open(board) as f:
                reader = csv.reader(f, delimiter=',')
                r = 0
                for row in reader:
                    c = 0
                    for square in row:
                        self.setSquare((r, c), int(square))
                        c += 1
                    r += 1

    def setBoard(self):
        self.board = []
        for row in range(self.size[0]):
            row = []
            for col in range(self.size[1]):
                row.append(None)
            self.board.append(row); 

    def getSize(self):
        return self.size
    
    def getSquare(self, index):
        return self.board[index[0]][index[1]]
    
    def setSquare(self, index, number):
        self.board[index[0]][index[1]] = number if number != 0 else None
    
    def solve(self):
        """
        Solves self in place
        """
        emptyIndex = self.getEmptyIndex()
        if not emptyIndex:
            return True
        for i in range(1, 10):
            if not self.isValidMove(emptyIndex, i):
                continue
            self.setSquare(emptyIndex, i)
            if self.solve():
                return True
            self.setSquare(emptyIndex, None)
        return False


    def isValidMove(self, index, number):
        row, col = index
        return not self.isInRow(row, number) and not self.isInCol(col, number) and not self.isInBox(index, number)
    
    def isInRow(self, row, number):
        for square in self.board[row]:
            if square == number:
                return True
        return False
    
    def isInCol(self, col, number):
        for row in self.board:
            square = row[col]
            if square == number:
                return True
        return False
    
    def isInBox(self, index, number):
        row, col = index
        while row % 3 != 0:
            row -= 1
        while col % 3 != 0:
            col -= 1
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                square = self.board[r][c]
                if square == number:
                    return True
        return False
    
    def getEmptyIndex(self):
        """Returns index of None, returns None if no None on board"""
        for row in range(self.rows):
            for col in range(self.cols):
                square = self.board[row][col]
                if not square:
                    return row, col
        return None