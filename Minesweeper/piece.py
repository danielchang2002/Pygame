class Piece:
    # States: Not clicked, clicked, flagged
    def __init__(self, hasBomb):
        self.hasBomb = hasBomb
        self.around = 0
        self.clicked = False
        self.flagged = False
        self.neighbors = []

    def __str__(self):
        return str(self.hasBomb)

    def getNumAround(self):
        return self.around

    def getHasBomb(self):
        return self.hasBomb

    def getClicked(self):
        return self.clicked

    def getFlagged(self):
        return self.flagged

    def toggleFlag(self):
        self.flagged = not self.flagged

    def handleClick(self):
        self.clicked = True

    def setNumAround(self):
        num = 0
        for neighbor in self.neighbors:
            if neighbor.getHasBomb():
                num += 1
        self.around = num

    def setNeighbors(self, neighbors):
        self.neighbors = neighbors
        
    def getNeighbors(self):
        return self.neighbors
 