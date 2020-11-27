import pygame
import sys
import math
# [x] Define L System
# [x] Implement Sentence Generation
# [x] Implement drawing
#   [x] Set up pygame
#   [x] Get command line input
#   [x] Implement draw function

# L Systems generate sentences, translate sentences into geometric structures
# Axiom: initial string
# produciton rules: generates longer strings 
# translate into geo structures

class LSystem():
    def __init__(self, axiom, rules, dtheta, start, length, ratio):
        self.sentence = axiom
        self.rules = rules
        self.theta = math.pi / 2
        self.dtheta = dtheta
        self.start = start
        self.x, self.y = start
        self.length = length
        self.ratio = ratio
        self.positions = []

    def __str__(self):
        return self.sentence

    def generate(self):
        self.x, self.y = self.start
        self.theta = math.pi / 2
        self.length *= self.ratio
        newStr = ""
        for char in self.sentence:
            mapped = char
            try:
                mapped = self.rules[char]
            except:
                pass
            newStr += mapped
        self.sentence = newStr

    def draw(self, screen):
        color = 0
        dcolor = 255 / len(self.sentence)
        for char in self.sentence:
            if char == 'F' or char == 'G':
                x2 = self.x - self.length * math.cos(self.theta)
                y2 = self.y - self.length * math.sin(self.theta)
                pygame.draw.line(screen, (255 - color, color, 125 + dcolor / 2), (self.x, self.y), (x2, y2))
                self.x, self.y = x2, y2
            elif char == '+':
                self.theta += self.dtheta
            elif char == '-':
                self.theta -= self.dtheta
            elif char == '[':
                self.positions.append({'x' : self.x, 'y' : self.y, 'theta' : self.theta})
            elif char == ']':
                position = self.positions.pop()
                self.x, self.y, self.theta = position['x'], position['y'], position['theta']
            color += dcolor

def main():
    l_sys_text = sys.argv[1]
    pygame.init()
    size = int(sys.argv[2]), int(sys.argv[3])
    start = int(sys.argv[4]), int(sys.argv[5])
    length = int(sys.argv[6])
    ratio = float(sys.argv[7])
    system = None
    with open(l_sys_text) as f:
        axiom = f.readline()
        numRules = int(f.readline())
        rules = {}
        for i in range(numRules):
            rule = f.readline().split(' ')
            rules[rule[0]] = rule[1]
        dTheta = math.radians(int(f.readline()))
        system = LSystem(axiom, rules, dTheta, start, length, ratio)
    screen = pygame.display.set_mode(size)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.fill((0, 0, 0))
                system.draw(screen)
                system.generate()
        pygame.display.flip()
    pygame.quit()

main()