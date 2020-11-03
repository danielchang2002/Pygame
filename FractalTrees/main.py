import pygame
import sys
import random
import math

dtheta = math.pi / 4
ratio = 0.7


def line(screen, x, y, len, theta):
    if (len >= 1):
        x2 = int(x - len * math.cos(theta))
        y2 = int(y - len * math.sin(theta))
        pygame.draw.line(screen, (len, 255 / len, 0), (x, y), (x2, y2))
        line(screen, x2, y2, len * ratio, theta - dtheta)
        line(screen, x2, y2, len * ratio, theta + dtheta)


pygame.init()

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode([WIDTH, HEIGHT])

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))

    line(screen, WIDTH / 2, HEIGHT, 150, math.pi / 2)
    pygame.display.flip()
    x, y = pygame.mouse.get_pos()
    dtheta = (x / 250) * math.pi
    ratio = (y / 500) * 0.7


pygame.quit()
