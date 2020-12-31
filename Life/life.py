import pygame
import math
from board import Board
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
WHITE = (255, 255, 255)
color = {}
color[0] = 15, 163, 177
color[1] = 181, 226, 250
color[2] = 249, 247, 243
color[3] = 237, 222, 164
color[4] = 247, 160, 114
color[5] = 247, 160, 114
color[6] = 242, 27, 63
color[7] = 70, 39, 73
color[8] = 51, 15, 10
class Life():
    def __init__(self, size):
        self.screenSize = 800, 800
        self.board = Board(size)
        self.pieceSize = self.screenSize[0] / size[1], self.screenSize[1] / size[0]
        

    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screenSize)
        running = True
        pygame.time.set_timer(pygame.USEREVENT, 200)
        started = False
        while running:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    running = False
                if (event.type == pygame.KEYDOWN):
                    started = True
                if (event.type == pygame.USEREVENT and started):
                    self.board.update()
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    position = pygame.mouse.get_pos()
                    self.handleClick(position)
            self.drawBoard()
            pygame.display.flip()
        pygame.quit()

    def drawBoard(self):
        self.screen.fill(BLACK)
        topLeft = (0, 0)
        b = self.board.getBoard()
        for row in b:
            for piece in row:
                rect = pygame.Rect(topLeft, self.pieceSize)
                pygame.draw.rect(self.screen, GREY, rect, width = 5)
                if piece.getAlive():
                    innerRect = pygame.Rect(topLeft[0] + 5, topLeft[1] + 5, self.pieceSize[0] - 10, self.pieceSize[1] - 10)
                    color = self.getColor(piece.getNumAroundAlive())
                    pygame.draw.rect(self.screen, color, innerRect)
                topLeft = topLeft[0] + self.pieceSize[0], topLeft[1]
            topLeft = 0, topLeft[1] + self.pieceSize[1]
                
    def handleClick(self, position):
        index = int(position[1] // self.pieceSize[1]), int(position[0] // self.pieceSize[0])
        self.board.handleClick(index)

    def getColor(self, numAlive):
        # return (255, abs(255 - numAlive * (255 / 4)), abs(255 - numAlive * (255 / 4)))
        return rgb(0, 8, numAlive)

def rgb(minimum, maximum, value):
    minimum, maximum = float(minimum), float(maximum)
    ratio = 2 * (value-minimum) / (maximum - minimum)
    b = int(max(0, 255*(1 - ratio)))
    r = int(max(0, 255*(ratio - 1)))
    g = 255 - b - r
    return r, g, b