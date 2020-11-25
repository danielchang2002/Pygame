import pygame
from time import sleep

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Block():
    def __init__(self, length, mass, velocity, left, bot):
        self.length = length
        self.mass = mass
        self.velocity = velocity
        self.left = left
        self.rect = pygame.Rect(left, bot - length, length, length)
        self.right = left + length

    def getPos(self): # left and right x coords
        return (self.left, self.right)

    def update(self, dt):
        self.left += self.velocity * dt
        self.right = self.left + self.length
    
    def switchDir(self):
        self.velocity = -1 * self.velocity

    def updateVisuals(self):
        self.rect.x = self.left

    def draw(self, screen):        
        pygame.draw.rect(screen, WHITE, self.rect)
        
    @staticmethod
    def collision(block1, block2):
        m1, v10, m2, v20 = block1.mass, block1.velocity, block2.mass, block2.velocity
        block1.velocity = (m1*v10+m2*v20-m2*v10+m2*v20)/(m1+m2)
        block2.velocity = (m1*v10+m2*v20-m1*v20+m1*v10)/(m1+m2)

class Sim():
    def __init__(self, digits):
        self.dim = 1600, 800
        pygame.init()
        self.screen = pygame.display.set_mode(self.dim)
        self.left = 10
        self.bot = self.dim[1] - 10
        # self.font = pygame.font.SysFont(None, 24)
        self.collisions = 0
        self.block1 = Block(50, 1, 0, self.dim[0]*(1/3), self.bot)
        self.block2 = Block(50 * digits, 100 ** (digits - 1), -30, self.dim[0]*(2/3), self.bot)
        self.line = (self.left, 0, self.left, self.dim[1])
        self.rate = 5

    def run(self):
        dt = 0.01
        running = True
        while running:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    running = False  
            self.screen.fill(BLACK)           
            pygame.draw.line(self.screen, WHITE, (10, 0), (10, self.bot))
            pygame.draw.line(self.screen, WHITE, (10, self.bot), (self.dim[0], self.bot)) 
            r = self.fastRate() if self.block2.left < self.left + (self.block1.length * 2) else self.rate
            for i in range(r):
                self.advance(dt)
                self.handleCollisions()
            self.updateVisuals()
            self.drawBlocks()
            pygame.display.flip()

        pygame.quit()

    def drawBlocks(self):
        self.block1.draw(self.screen)
        self.block2.draw(self.screen)

    def fastRate(self):
        dist = self.block2.left - (self.left + self.block1.length)
        return int((self.rate * 10) / dist)

    def updateVisuals(self):
        self.block1.updateVisuals()
        self.block2.updateVisuals()

    def advance(self, dt):
        self.block1.update(dt)
        self.block2.update(dt)
        
    def handleCollisions(self):
        collision = False
        if self.block1.left < self.left:
            distError = self.block1.left - self.left
            timeError = distError / self.block1.velocity
            self.advance(-timeError)
            self.block1.switchDir()
            collision = True
        elif self.block1.right > self.block2.left:
            timeError = (self.block1.right-self.block2.left)/(self.block1.velocity-self.block2.velocity)
            self.advance(-timeError)
            Block.collision(self.block1, self.block2)
            collision = True
        if collision:
            self.collisions += 1
            self.drawNumber()

    def drawNumber(self):
        # img = font.render(str(self.collisions), True, WHITE)
        # self.screen.blit(img, (WIDTH - 100, 50))
        print(self.collisions)

sim = Sim(5)
sim.run()
