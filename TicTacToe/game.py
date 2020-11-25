import pygame
from board import Board

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

BUFFER = 10

class Game:
    def __init__(self, dim):
        self.dim = dim
        self.screen = pygame.display.set_mode(dim)
        self.board = Board()
        self.player = 'O'
        self.comp = 'X'

    def run(self):
        pygame.init()
        running = True
        while running:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    running = False
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    self.handleClick(pygame.get_pos())
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()

        pygame.quit()

    def draw(self):
        self.drawLines()
        self.drawPieces()

    def drawLines(self):
        width, height = self.dim[0], self.dim[1]
        x1, x2 = width * (1/3), width * (2/3)
        y1, y2 = height * (1/3), height * (2/3)
        pygame.draw.line(self.screen, WHITE, (0, y1), (width, y1))
        pygame.draw.line(self.screen, WHITE, (0, y2), (width, y2))
        pygame.draw.line(self.screen, WHITE, (x1, 0), (x1, height))
        pygame.draw.line(self.screen, WHITE, (x2, 0), (x2, height))

    def drawPieces(self):
        for i in range(9):
            piece = self.board.board[i]
            if piece == '-':
                continue
            region = self.getRegion(i)
            if piece == 'O':
                self.drawO(region)
            else:
                self.drawX(region)

    def getRegion(self, i):
        width, height = self.dim[0] / 3, self.dim[1] / 3
        x1 = (i % 3) * width
        y1 = (i // 3) * height
        return (x1 + BUFFER, y1 + BUFFER, x1 + width - BUFFER, y1 + height - BUFFER)

    def drawO(self, region):
        width = region[2] - region[0]
        height = region[3] - region[1]
        rect = pygame.Rect(region[0], region[1], width, height)
        pygame.draw.ellipse(self.screen, RED, rect, 5)

    def drawX(self, region):
        pygame.draw.line(self.screen, GREEN, (region[0], region[1]), (region[2], region[3]), width = 5)
        pygame.draw.line(self.screen, GREEN, (region[2], region[1]), (region[0], region[3]), width = 5)
    
    def getI(self, pos):
        pass

    def handleClick(self, pos):
        i = getI(pos)
        self.board.move(i)
            


g = Game((500, 500))
g.run()