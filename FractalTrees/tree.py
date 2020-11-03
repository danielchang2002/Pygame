import pygame
import math

pygame.init()

WIDTH = 600
HEIGHT = 500
r = 0.67
deltaTheta = math.pi / 6


screen = pygame.display.set_mode([WIDTH, HEIGHT])


def line(screen, x, y, length, theta):
    if (length <= 1):
        return
    x2 = x - length * math.cos(theta)
    y2 = y - length * math.sin(theta)
    pygame.draw.line(screen, (length, 255 / length, 0), (x, y), (x2, y2))
    line(screen, x2, y2, length * r, theta + deltaTheta)
    line(screen, x2, y2, length * r, theta - deltaTheta)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    line(screen, WIDTH / 2, HEIGHT, 150, math.pi / 2)

    x, y = pygame.mouse.get_pos()

    r = (y / 500) * 0.7
    deltaTheta = (x / 250) * math.pi

    pygame.display.flip()

pygame.quit()
