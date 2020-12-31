import pygame
from board import Board
from time import sleep
from solver import Solver

RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

class Game():
    def __init__(self, screenSize):
        self.screenSize = screenSize
        self.pieceSize = self.screenSize[0] / 3, self.screenSize[1] / 3
        self.player = 'O'
        self.computer = 'X'
        self.board = Board(None)
        self.compTurn = False
        self.state = 'ask'

    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screenSize)
        running = True
        while running:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    running = False
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    self.handleClick(pygame.mouse.get_pos())
            if (self.state == 'game'):
                self.game()
            else:
                self.ask()
            pygame.display.flip()
        pygame.quit()
    
    def ask(self):
        self.screen.fill((0, 0, 0))
        self.drawX((1, 0))
        self.drawO((1, 2))
    
    def game(self):
        self.draw()
        if (self.checkEnd()):
            self.state = 'ask'
            self.board = Board(None)
            self.compTurn = False
        if (self.compTurn):
            self.compMove()
    
    def checkEnd(self):
        winBoard = ()
        if (self.board.getHasWon(self.player)):
            winBoard = self.board.getHasWon(self.player)
        elif (self.board.getHasWon(self.computer)):
            winBoard = self.board.getHasWon(self.computer)
        elif (not self.board.isFull()):
            return False
        for row, col in winBoard:
            self.highlight((row, col))
        pygame.display.flip()
        sleep(3)
        return True


    def highlight(self, index):
        region = self.getRegion(index)
        pygame.draw.rect(self.screen, BLUE, region, width = 10)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.drawPieces()
        self.drawLines()

    def drawPieces(self):
        for row in range(3):
            for col in range(3):
                piece = self.board.getPiece((row, col))
                if (piece == 'X'):
                    self.drawX((row, col))
                elif (piece == 'O'):
                    self.drawO((row, col))

    def drawX(self, index):
        region = self.getRegion(index)
        pygame.draw.line(self.screen, RED, region.topleft, region.bottomright, width = 10)
        pygame.draw.line(self.screen, RED, region.topright, region.bottomleft, width = 10)

    def drawO(self, index):
        region = self.getRegion(index)
        pygame.draw.ellipse(self.screen, GREEN, region, width=10)
    
    def getRegion(self, index):
        buffer = 10
        leftTop = int(index[1] * self.pieceSize[0] + buffer), int(index[0] * self.pieceSize[1] + buffer)
        widthHeight = int(self.pieceSize[0] - buffer), int(self.pieceSize[1] - buffer)
        rect = pygame.Rect(leftTop, widthHeight)
        return rect
    
    def drawLines(self):
        for i in range(1, 3):
            x = i * (self.screenSize[0] / 3)
            pygame.draw.line(self.screen, WHITE, (x, 0), (x, self.screenSize[1]), width = 10)
        for i in range(1, 3):
            y = i * (self.screenSize[1] / 3)
            pygame.draw.line(self.screen, WHITE, (0, y), (self.screenSize[0], y), width = 10) 

    def getIndex(self, position):
        return int(position[1] / self.pieceSize[1]), int(position[0] / self.pieceSize[0])

    def handleClick(self, position):
        if (self.state == 'ask'):
            if (position[0] < self.screenSize[0] / 2):
                self.player = 'X'
                self.computer = 'O'
                self.compTurn = False
            else:
                self.player = 'O'
                self.computer = 'X'
                self.compTurn = True
            self.state = 'game'
            return
        index = self.getIndex(position)
        piece = self.board.getPiece(index)
        if (piece != '-'):
            return 
        self.board = self.board.getMovedBoard(index, self.player)
        self.compTurn = True
    
    def compMove(self):
        solver = Solver()
        self.board = solver.getBestMove(self.board, self.computer)
        self.compTurn = False
    