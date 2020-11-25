from typing import List
from typing import Dict
import pygame
import math
import sys
# [x] Define LSystem
# [x] Implement Sentence Generation
# [] Implement drawing

# Axiom: Initial String
# Production Rules: Change the String Iteratively
# Make geometric structures using the string


class LSystem():
    def __init__(self, axiom: str, rules: Dict[str, str], start: tuple, length: int, theta: int):
        self.sentence = axiom
        self.rules = rules
        self.x = start[0]
        self.y = start[1]
        self.length = length
        self.dtheta = math.radians(theta)
        self.theta = math.pi / 2
        self.positions = []

    def __str__(self):
        return self.sentence

    def generate(self):
        newSentence = ""
        for char in self.sentence:
            mapped = ""
            try:
                mapped = self.rules[char]
            except:
                mapped = char
            newSentence += mapped
        self.sentence = newSentence

    def draw(self, screen):
        for char in sentence:
            if char == 'F' or char == 'G':
                x2 = self.x + length * math.cos(theta)
                y2 = self.y + length * math.sin(theta)
                pygame.draw.line(screen, (255, 255, 255), self.x, self.y, x2, y2)
                self.x = x2
                self.y = y2
            if char == '+':
                self.theta += self.dtheta
            if char == '-':
                self.theta -= self.dtheta
            if char == '[':
                self.positions.append({'x' : self.x, 'y' : self.y, 'theta' : self.theta})
            if char == ']':
                positions = self.positions.pop()
                self.x = positions['x']
                self.y = positions['y']
                self.theta = positions['theta']



def main():
    systemFile = sys.arg[0]
    sizeScreen = int(sys.arg[1]), int(sys.arg[2])
    start = int(sys.arg[3]), int(sys.arg[4])
    length = int(sys.arg[5])
    pygame.init()
    screen = pygame.display.set_mode(sizeScreen)
    system = None
    with open(systemFile) as f:
        axiom = f.readLine()
        numRules = int(f.readLine())
        rules = {}
        for i in range(numRules):
            rule = f.readLine().split(' ')
            rules[rule[0]] = rule[1]
        system = LSystem(axiom, rules, start, length, int(f.readLine()))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                system.draw(screen)
                system.generate()
        pygame.display.flip()
    pygame.quit()
        
if __name__ == '__main__':
    main()
