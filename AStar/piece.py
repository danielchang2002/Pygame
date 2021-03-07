from math import inf

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
        self.g = inf
        self.h = inf
        self.timePopped = -1
    
    def setNeighbors(self, neighbors):
        self.neighbors = neighbors
    
    def f(self):
        return self.g + self.h
    
    def __lt__(self, other):
        return self.f() < other.f()


    

