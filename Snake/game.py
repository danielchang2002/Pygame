import pygame
from snake import Snake
from block import Block
from random import random

RED = 255, 0, 0
WHITE = 255, 255, 255
BLACK = 0, 0, 0

class Game():
    def __init__(self, rows, cols):
        self.screenWidth, self.screenHeight = 800, 800
        self.numRows, self.numCols = rows, cols
        self.blockWidth, self.blockHeight = self.screenWidth / self.numRows, self.screenHeight / self.numRows
        self.snake = Snake(self.numRows // 2, self.numCols // 2, WHITE)
        self.apple = Block(self.numRows // 4, self.numCols // 4, RED)
        self.interval = 350

    def run(self):
        pygame.init()
        self.STEP = pygame.USEREVENT + 1
        pygame.time.set_timer(self.STEP, self.interval)
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        running = True
        while running:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    running = False
                elif (event.type == pygame.KEYDOWN):
                    if event.key == pygame.K_w:
                        self.snake.v_y = -1
                        self.snake.v_x = 0
                    elif event.key == pygame.K_a:
                        self.snake.v_y = 0
                        self.snake.v_x = -1
                    elif event.key == pygame.K_s:
                        self.snake.v_y = 1
                        self.snake.v_x = 0
                    elif event.key == pygame.K_d:
                        self.snake.v_y = 0
                        self.snake.v_x = 1
                elif (event.type == self.STEP and self.snake.alive):
                    self.snake.step(False)
            self.snake.checkCollisions(self.numRows, self.numCols)
            self.screen.fill(BLACK)
            self.checkApple()
            self.drawSnake()
            self.drawApple()
            pygame.display.flip()
        pygame.quit()

    def drawSnake(self):
        for block in self.snake.blocks:
            rect = pygame.Rect(self.getLeftTop(block.x, block.y), (self.blockWidth, self.blockHeight))
            pygame.draw.rect(self.screen, block.color, rect)

    def drawApple(self):
        rect = pygame.Rect(self.getLeftTop(self.apple.x, self.apple.y), (self.blockWidth, self.blockHeight))
        pygame.draw.rect(self.screen, self.apple.color, rect)

    def getLeftTop(self, x, y):
        return (x / self.numRows) * self.screenWidth, (y / self.numRows) * self.screenHeight
    
    def checkApple(self):
        if self.snake.head.equals(self.apple):
            self.snake.step(True)
            self.apple = Block((int) (random() * self.numCols), (int) (random() * self.numRows), RED)
            self.interval *= 0.9
            pygame.time.set_timer(self.STEP, (int) (self.interval))



if __name__ == '__main__':
    g = Game(20, 20)
    g.run()