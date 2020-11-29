import pygame
from piece import Piece 
from board import Board 
import os

class Game:
    def __init__(self, size, prob):
        self.board = Board(size, prob)
        pygame.init()
        self.sizeScreen = 800, 800
        self.screen = pygame.display.set_mode(self.sizeScreen)
        self.pieceSize = (self.sizeScreen[0] / size[1], self.sizeScreen[1] / size[0]) 
        self.loadPictures()

    def loadPictures(self):
        self.images = {}
        for root, subdir, files in os.walk("images"):
            if len(files) <= 1:
                continue
            for fileName in files:
                path = root + r'/' + fileName
                with open(path) as f:
                    img = pygame.image.load(path)
                    img = img.convert()
                    img = pygame.transform.scale(img, (int(self.pieceSize[0]), int(self.pieceSize[1])))
                    self.images[fileName.split(".")[0]] = img
            
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    rightClick = pygame.mouse.get_pressed(num_buttons=3)[2]
                    self.handleClick(pygame.mouse.get_pos(), rightClick)
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()
        pygame.quit()

    def draw(self):
        topLeft = (0, 0)
        for row in self.board.getBoard():
            for piece in row:
                rect = pygame.Rect(topLeft, self.pieceSize)
                image = None
                if piece.getClicked():
                    image = self.images[str(piece.getNumAround()) if not piece.getHasBomb() else 'bomb-at-clicked-block']
                else:
                    image = self.images['flag' if piece.getFlagged() else 'empty-block']
                self.screen.blit(image, topLeft) 
                topLeft = topLeft[0] + self.pieceSize[0], topLeft[1]
            topLeft = (0, topLeft[1] + self.pieceSize[1])

    def handleClick(self, position, flag):
        index = tuple(int(pos // size) for pos, size in zip(position, self.pieceSize))[::-1] 
        self.board.handleClick(self.board.getPiece(index), flag)
