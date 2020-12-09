import pygame
from board import Board
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
WHITE = (255, 255, 255)
class Life():
    def __init__(self, size):
        self.screenSize = 800, 800
        self.board = Board(size)
        self.pieceSize = self.screenSize[0] / size[1], self.screenSize[1] / size[0]
        

    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screenSize)
        running = True
        while running:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    running = False
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    self.board.update()
            self.drawBoard()
            pygame.display.flip()
        pygame.quit()

    def drawBoard(self):
        topLeft = (0, 0)
        b = self.board.getBoard()
        for row in b:
            for piece in row:
                rect = pygame.Rect(topLeft, self.pieceSize)
                pygame.draw.rect(self.screen, GREY, rect, width = 5)
                if piece.getAlive():
                    innerRect = pygame.Rect(topLeft[0] + 5, topLeft[1] + 5, self.pieceSize[0] - 10, self.pieceSize[1] - 10)
                    pygame.draw.rect(self.screen, WHITE, innerRect)
                topLeft = topLeft[0] + self.pieceSize[0], topLeft[1]
            topLeft = 0, topLeft[1] + self.pieceSize[1]
                

