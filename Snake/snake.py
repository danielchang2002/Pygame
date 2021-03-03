from block import Block

class Snake:
    def __init__(self, x, y, color):
        self.color = color
        self.blocks = [Block(x - 2, y, color), Block(x - 1, y, color), Block(x, y, color)]
        self.head = self.blocks[-1]
        self.v_x, self.v_y = 1, 0
        self.alive = True
    
    def step(self, apple):
        self.blocks.append(Block(self.blocks[-1].x + self.v_x, self.blocks[-1].y + self.v_y, self.color))
        if not apple:
            self.blocks = self.blocks[1:]
        self.head = self.blocks[-1]
    
    def checkCollisions(self, numRows, numCols):
        if self.head.x >= numCols or self.head.y >= numRows \
        or self.head.x < 0 or self.head.y < 0:
            self.alive = False
            return
        for block in self.blocks[:-1]:
            if block.equals(self.head):
                self.alive = False
                return
    
    
