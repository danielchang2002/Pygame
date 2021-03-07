from piece import Piece
import sys
import pygame
from collections import deque
from queue import PriorityQueue
import heapq
from math import exp

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
        for r in range(max(piece.row - 1, 0), min(piece.row + 2, self.rows)):
            for c in range(max(piece.col - 1, 0), min(piece.col + 2, self.cols)):
                if r == piece.row and c == piece.col:
                    continue
                n.append(self.board[r][c])
        # if (piece.row - 1 >= 0):
        #     n.append(self.board[piece.row - 1][piece.col])
        # if (piece.row + 1 < self.rows):
        #     n.append(self.board[piece.row + 1][piece.col])
        # if (piece.col - 1 >= 0):
        #     n.append(self.board[piece.row][piece.col - 1])
        # if (piece.col + 1 < self.cols):
        #     n.append(self.board[piece.row][piece.col + 1])
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
                    pygame.time.set_timer(self.STEP, 10)
                if event.type == self.STEP and not self.done:
                    # self.BFSStep()
                    self.AStarStep()
            self.screen.fill(WHITE)
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
    
    def AStarStep(self):
        # self.printBoard()
        # self.pq.sort(key=lambda x: x.f(),reverse=True)
        # piece = self.pq.pop()
        piece = heapq.heappop(self.pq)
        piece.timePopped = pygame.time.get_ticks()
        piece.popped = True
        piece.visited = True
        if piece.isEnd:
            curr = piece
            self.done = True
            while not curr.isStart:
                curr.path = True
                curr = curr.parent
            return
        for neighbor in piece.neighbors:
            if neighbor.popped or neighbor.isWall:
                continue
            diag = piece.row != neighbor.row and piece.col != neighbor.col
            g = piece.g + (14 if diag else 10)
            h = self.euclidean(neighbor, self.end)
            if (g < neighbor.g or not neighbor.visited):
                neighbor.g = g
                neighbor.h = h
                neighbor.parent = piece
                if (not neighbor.visited):
                    # self.pq.append(neighbor)
                    heapq.heappush(self.pq, neighbor)
            neighbor.visited = True

    def manhattan(self, curr, target):
        return abs(curr.row - target.row) + abs(curr.col - target.col)
    
    def euclidean(self, first, second):
        dy = abs(first.row - second.row)
        dx = abs(first.col - second.col)
        diag = min(dy, dx)
        return diag * 14 + (max(dy, dx) - diag) * 10
    
    def printBoard(self):
        for r in range(self.rows):
            for c in range(self.cols):
                print(self.board[r][c].f(), end=" ")
            print()
        pass

    def handleClick(self, pos):
        x, y = pos
        col, row = int(self.cols * x / self.screenWidth), int(self.rows * y / self.screenHeight)
        piece = self.board[row][col]
        if self.modes[self.mode] == 'begin':
            self.start = piece
            self.start.isStart = True
            self.q = deque()
            self.q.append(piece)
            piece.g = 0
            self.pq = [piece]
            # self.pq.sort(reverse=True)
            heapq.heapify(self.pq)
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
            pygame.draw.rect(self.screen, RED, rect)
        elif piece.path:
            pygame.draw.rect(self.screen, YELLOW, rect)
        elif piece.isWall:
            pygame.draw.rect(self.screen, BLACK, rect)
        elif piece.popped:
            sincePopped = pygame.time.get_ticks() - piece.timePopped
            val = exp(sincePopped * 0.01)
            # val = sincePopped * 1000 / 255
            RGB = (0, min(val, 255), min(val, 255))
            pygame.draw.rect(self.screen, RGB, rect)
        # elif piece.visited:
            # pygame.draw.rect(self.screen, RED, rect)
        else:
            pygame.draw.rect(self.screen, BLACK, rect, width = 1)

if __name__ == '__main__':
    rows, cols = int(sys.argv[1]), int(sys.argv[2])
    sim = Sim((rows, cols))
    sim.run()