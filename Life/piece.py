class Piece():
    def __init__(self, alive):
        self.alive = alive

    def getAlive(self):
        return self.alive
    
    def setNeighbors(self, neighbors):
        self.neighbors = neighbors

    def getNeighbors(self):
        return self.neighbors

    def setAlive(self, alive):
        self.alive = alive

    def getNumAroundAlive(self):
        alive = 0
        for neighbor in self.neighbors:
            if neighbor.getAlive():
                alive += 1
        return alive

    def toggle(self):
        self.alive = not self.alive