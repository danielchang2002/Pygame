import pygame
import math
import random
import time


class LSystem:
    def __init__(self, axiom, rules, x, y, length):
        self.axiom = axiom
        self.sentence = axiom
        self.rules = rules
        self.x = x
        self.y = y
        self.theta = math.pi / 2
        self.length = length
        self.dtheta = math.pi / 6
        self.stack = []

    def generate(self):
        self.x = 250
        self.y = 500
        self.theta = math.pi / 2
        self.length *= 0.5
        newSent = ''
        for char in self.sentence:
            match = False
            for rule in self.rules:
                if (rule['in'] == char):
                    newSent += rule['out']
                    match = True
                    break
            if (not match):
                newSent += char
        self.sentence = newSent

    def printSent(self):
        print(self.sentence)

    def draw(self, screen):
        # font = pygame.font.SysFont(None, 12)
        # print(self.sentence)
        # print(self.x, self.y, self.theta)
        color = 0
        dcolor = 255 / len(self.sentence)
        for char in self.sentence:
            # print(char)
            if (char == 'F'):
                x2 = self.x - self.length * math.cos(self.theta)
                y2 = self.y - self.length * math.sin(self.theta)
                pygame.draw.line(screen, (color, 255 - color, 100 + color / 255, 100),
                                 (self.x, self.y), (x2, y2))

                # img = font.render(
                #     # str(self.x) + " " + str(self.y) + " " +
                #     str(self.theta), True, (0, 0, 255, 0))
                # screen.blit(img, ((self.x + x2) / 2, (self.y + y2) / 2))

                self.x = x2
                self.y = y2
                # print(self.x, self.y, self.theta)
            elif (char == '+'):
                self.theta += self.dtheta
                # print(self.x, self.y, self.theta)
            elif (char == '-'):
                self.theta -= self.dtheta
                # print(self.x, self.y, self.theta)
            elif (char == '['):
                self.stack.append(
                    {'x': self.x, 'y': self.y, 'theta': self.theta})
                # print(self.x, self.y, self.theta)
            else:
                dict = self.stack.pop()
                self.x = dict['x']
                self.y = dict['y']
                self.theta = dict['theta']
                # print(self.x, self.y, self.theta)
            color += dcolor
            # pygame.display.update()
            # time.sleep(0.01)


axiom = 'F'
sentence = axiom
rules = [{}]
rules[0] = {
    'in': 'F',
    'out': 'FF+[+F-F-F]-[-F+F+F]'
}


pygame.init()
screen = pygame.display.set_mode([500, 500])

length = 150

myLSystem = LSystem(axiom, rules, 250, 500, length)

first = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((255, 255, 255))
            myLSystem.draw(screen)
            myLSystem.printSent()
            myLSystem.generate()

    if (first):
        screen.fill((255, 255, 255))
        first = False

    pygame.display.flip()

pygame.quit()
