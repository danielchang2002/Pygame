class Board():
    def __init__(self, size):
        self.size = size;
        self.setBoard();

    def setBoard(self):
        self.board = [];
        for row in range(self.size[0]):
            row = []
            for col in range(self.size[1]):
                row.append(None)
            self.board.append(row); 

    def getSize(self):
        return self.size
    
    def getSquare(self, index):
        return self.board[index[0]][index[1]]