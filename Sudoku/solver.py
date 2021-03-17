import pygame

BLACK = 0, 0, 0

class Solver():
    def __init__(self, board):
        self.width, self.height = 800, 800
        self.board = board
        self.rows, self.cols = self.board.getSize()
        self.squareWidth, self.squareHeight = self.width / self.cols, self.height / self.rows
        self.hRow, self.hCol = 0, 0
        self.setImgs()

    def setImgs(self):
        pygame.font.init()
        font = pygame.font.SysFont('kameron', 64)
        self.imgs = {}
        for i in range(1, 10):
            img = font.render(str(i), True, BLACK)
            self.imgs[str(i)] = img

    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        running = True
        while running:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    running = False
                    break
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    self.handleClick(pygame.mouse.get_pos())
                if (event.type == pygame.KEYDOWN):
                    self.handleKey(event)
            self.screen.fill((255, 255, 255))
            self.draw()
            pygame.display.flip()
        pygame.quit()

    def handleClick(self, pos):
        x, y = pos
        self.hRow, self.hCol = int(self.rows * (y / self.height)), int(self.cols * (x / self.width))

    def handleKey(self, event):
        if event.scancode == 42:
            self.board.setSquare((self.hRow, self.hCol), None)
        if event.scancode == 40:
            solved = self.board.solve()
            return
        key = event.unicode
        if key == 'w':
            self.hRow = (self.hRow - 1) % self.rows
        elif key == 'a':
            self.hCol = (self.hCol - 1) % self.cols
        elif key == 's':
            self.hRow = (self.hRow + 1) % self.rows
        elif key == 'd':
            self.hCol = (self.hCol + 1) % self.cols
        try:
            number = int(key)
        except ValueError:
            return
        if number < 1 or number > 9:
            return
        self.board.setSquare((self.hRow, self.hCol), number)

    def draw(self):
        left, top = 0, 0
        for row in range(self.rows):
            for col in range(self.cols):
                number = self.board.getSquare((row, col))
                rect = pygame.Rect((left, top), (self.squareWidth, self.squareHeight))
                if row == self.hRow and col == self.hCol:
                    RGB = (187,222,251)
                    width = 0
                    pygame.draw.rect(self.screen, RGB, rect, width=width)
                RGB = 100, 100, 100
                width = 10
                pygame.draw.rect(self.screen, RGB, rect, width=width)
                if number:
                    img = self.imgs[str(number)]
                    w, h = img.get_size()
                    centerX, centerY = left + self.squareWidth * 0.5, top + self.squareHeight * 0.5
                    self.screen.blit(img, (centerX - 0.5 * w, centerY - 0.5 * h))
                left, top = left + self.squareWidth, top
            left, top = 0, top + self.squareHeight
        self.drawLines()

    def drawLines(self):
        x0, y0 = self.width, self.height
        for i in range(1, 3):
            x = i * (x0 / 3)
            pygame.draw.line(self.screen, (50, 50, 50), (x, 0), (x, y0), width = 15)
        for i in range(1, 3):
            y = i * (y0 / 3)
            pygame.draw.line(self.screen, (50, 50, 50), (0, y), (x0, y), width = 15)
