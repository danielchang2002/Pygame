import re
from LSystem import LSystem
import math
import pygame

systems = []

with open('Lsystems.txt') as text:
    for line in text:
        stringList = re.split(',|\n', line)
        axiom = stringList[1]
        angle = math.radians(int(stringList[2]))
        length = int(stringList[3])
        x, y = int(stringList[4]), int(stringList[5])
        rulesList = stringList[6].split()
        rules = []
        for rule in rulesList:
            rules.append({
                'in': rule.split('->')[0],
                'out': rule.split('->')[1]
            })
        systems.append(LSystem(axiom, rules, x, y, length, angle))


curr = systems[4]

pygame.init()
screen = pygame.display.set_mode([500, 500])


first = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((255, 255, 255))
            curr.draw(screen)
            curr.printSent()
            curr.generate()

    if (first):
        screen.fill((255, 255, 255))
        first = False

    pygame.display.flip()

pygame.quit()
