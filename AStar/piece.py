class Piece:
    def __init__(self, row, col):
        self.row, self.col = row, col
        self.isStart = False
        self.isWall = False
        self.isEnd = False
        self.visited = False
        self.popped = False
        self.parent = None
        self.path = False
    
    def setNeighbors(self, neighbors):
        self.neighbors = neighbors
    

    

