from piece import Piece
import sys
import pygame
from collections import deque

WHITE = 255, 255, 255
BLACK = 0, 0, 0
CYAN = 0, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
YELLOW = 255, 255, 0

class Sim:
    def __init__(self, size):
        self.screenWidth, self.screenHeight = 800, 800
        self.rows, self.cols = size[0], size[1]
        self.pieceWidth, self.pieceHeight = self.screenWidth / self.cols, self.screenHeight / self.rows
        self.modes = 'begin', 'end', 'wall', 'start'
        self.mode = 0
        self.done = False
        self.drag = False
        self.STEP = pygame.USEREVENT+1
        self.setBoard()
    
    def setBoard(self):
        self.board = []
        for r in range(self.rows):
            row = [] 
            for c in range(self.cols):
                row.append(Piece(r, c))
            self.board.append(row)    
        for row in self.board:
            for piece in row:
                neighbors = self.getNeighborsList(piece)
                piece.setNeighbors(neighbors)

    def getNeighborsList(self, piece):
        n = []
        # for r in range(max(piece.row - 1, 0), min(piece.row + 2, self.rows)):
        #     for c in range(max(piece.col - 1, 0), min(piece.col + 2, self.cols)):
        #         if r == piece.row and c == piece.col:
        #             continue
        #         n.append(self.board[r][c])
        if (piece.row - 1 >= 0):
            n.append(self.board[piece.row - 1][piece.col])
        if (piece.row + 1 < self.rows):
            n.append(self.board[piece.row + 1][piece.col])
        if (piece.col - 1 >= 0):
            n.append(self.board[piece.row][piece.col - 1])
        if (piece.col + 1 < self.cols):
            n.append(self.board[piece.row][piece.col + 1])
        return n

    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN or self.drag:
                    self.handleClick(pygame.mouse.get_pos())
                if event.type == pygame.MOUSEBUTTONUP:
                    self.drag = False
                if event.type == pygame.KEYDOWN:
                    self.mode = 3
                    pygame.time.set_timer(self.STEP, 250)
                if event.type == self.STEP and not self.done:
                    self.BFSStep()
            self.screen.fill(BLACK)
            self.drawBoard()
            pygame.display.flip()
        pygame.quit()
    
    def BFSStep(self):
        length = len(self.q) 
        for i in range(length):
            piece = self.q.popleft()
            piece.popped = True
            piece.visited = True
            for neighbor in piece.neighbors:
                if neighbor.visited or neighbor.isWall:
                    continue
                neighbor.parent = piece
                if neighbor.isEnd:
                    self.done = True
                    curr = neighbor
                    while curr:
                        curr.path = True
                        curr = curr.parent
                    return
                self.q.append(neighbor)
                neighbor.visited = True

    def handleClick(self, pos):
        x, y = pos
        col, row = int(self.rows * x / self.screenWidth), int(self.cols * y / self.screenHeight)
        piece = self.board[row][col]
        if self.modes[self.mode] == 'begin':
            self.start = piece
            self.start.isStart = True
            self.q = deque()
            self.q.append(piece)
            self.mode += 1
        elif self.modes[self.mode] == 'end':
            self.end = piece
            self.end.isEnd = True
            self.mode += 1
        elif self.modes[self.mode] == 'wall':
            self.drag = True
            piece.isWall = True

    def drawBoard(self):
        for row in self.board:
            for piece in row:
                self.drawPiece(piece)

    def drawPiece(self, piece):
        leftTop = self.pieceWidth * piece.col, self.pieceHeight * piece.row
        rect = pygame.Rect(leftTop, (self.pieceWidth, self.pieceHeight))
        if piece.isStart or piece.isEnd:
            pygame.draw.rect(self.screen, CYAN, rect)
        elif piece.path:
            pygame.draw.rect(self.screen, YELLOW, rect)
        elif piece.isWall:
            pygame.draw.rect(self.screen, BLUE, rect)
        elif piece.popped:
            pygame.draw.rect(self.screen, GREEN, rect)
        elif piece.visited:
            pygame.draw.rect(self.screen, RED, rect)
        else:
            pygame.draw.rect(self.screen, WHITE, rect, width = 2)

if __name__ == '__main__':
    rows, cols = int(sys.argv[1]), int(sys.argv[2])
    sim = Sim((rows, cols))
    sim.run()