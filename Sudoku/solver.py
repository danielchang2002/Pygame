import pygame

class Solver():
    def __init__(self, board):
        self.board = board

    def run(self):
        pygame.init()
        self.size = 800, 800
        self.screen = pygame.display.set_mode(self.size)

        running = True
        while running:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    running = False
            self.screen.fill((255, 255, 255))
            self.draw()
            pygame.display.flip()
        pygame.quit()
    
    def draw(self):
        topLeft = (0, 0)
        boardSize = self.board.getSize()
        squareSize = self.size[0] / boardSize[1], self.size[1] / boardSize[0] 
        for row in range(boardSize[0]):
            for col in range(boardSize[1]):
                rect = pygame.Rect(topLeft, squareSize)
                pygame.draw.rect(self.screen, (100, 100, 100), rect, width=10)
                topLeft = topLeft[0] + squareSize[0], topLeft[1]
            topLeft = 0, topLeft[1] + squareSize[1]
        self.drawLines()

    def drawLines(self):
        x0, y0 = self.size
        for i in range(1, 3):
            x = i * (x0 / 3)
            pygame.draw.line(self.screen, (50, 50, 50), (x, 0), (x, y0), width = 15)
        for i in range(1, 3):
            y = i * (y0 / 3)
            pygame.draw.line(self.screen, (50, 50, 50), (0, y), (x0, y), width = 15)