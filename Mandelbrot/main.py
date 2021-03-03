import pygame
import numpy as np
from math import sqrt

def mandelbrot(a, b, iters, bound):
    originalA = a
    originalB = b
    for i in range(iters):
        aTemp = a**2 - b**2 + originalA
        b = 2 * a * b + originalB
        a = aTemp
        if (a**2 + b**2 >= bound):
            return i
    return iters

width, height = 500, 300

minX, maxX, minY, maxY = -2.5, 1, -1, 1

def getColor(n, maxIters):
    c = sqrt(n / maxIters) * 360
    color = pygame.Color(0, 0, 0)
    color.hsva = c, 100, 100, 100
    return color.r, color.g, color.b

def getGrid():
    mandelbrotGrid = np.zeros((width, height, 3))
    maxIters = 50
    for x in range(width):
        for y in range(height):
            a = minX + (x / width) * (maxX - minX)
            b = minY + (y / height) * (maxY - minY)
            n = mandelbrot(a, b, maxIters, 4)
            mandelbrotGrid[x, y] = 0 if n == maxIters else getColor(n, maxIters)
    return mandelbrotGrid

grid = getGrid()

pygame.init()
screen = pygame.display.set_mode((width, height))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            x = minX + (maxX - minX) * (x / width)
            y = minY + (maxY - minY) * (y / height)
            minX = minX + (x - minX) * 0.8
            maxX = maxX - (maxX - x) * 0.8
            minY = minY + (y - minY) * 0.8
            maxY = maxY - (maxY - y) * 0.8
            grid = getGrid()
            break
    pygame.surfarray.blit_array(screen, grid)
    pygame.display.flip()
pygame.quit()
