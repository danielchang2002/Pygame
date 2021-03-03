import pygame
import numpy as np
from math import sqrt

def mandelbrot(a, b, iters, bound, ca, cb):
    """
    Runs iters iterations of the mandelbrot function, f(z) = z^2 + c,
    where c = a + bi. Returns number of iterations that a**2 + b**2 < bound
    """
    # a^2 - b^2 + 2abi + a + bi
    for i in range(iters):
        aTemp = a**2 - b**2 + ca
        b = 2 * a * b + cb
        a = aTemp
        if (a**2 + b**2 >= bound):
            return i
    return iters

width, height = 800, 500
minX, maxX, minY, maxY = -1.5, 1.5, -1, 1

def getGrid(ca, cb):
    mandelbrotGrid = np.zeros((width, height, 3))
    maxIters = 50
    for x in range(width):
        for y in range(height):
            a = minX + (x / width) * (maxX - minX)
            b = minY + (y / height) * (maxY - minY)
            n = mandelbrot(a, b, maxIters, 4, ca, cb)
            color = 0
            if n != maxIters:
                c = sqrt(n / maxIters) * 360
                color = pygame.Color(0, 0, 0)
                color.hsva = c, 100, 100, 100
                mandelbrotGrid[x, y] = color.r, color.g, color.b
            else:
                mandelbrotGrid[x, y] = 0
    return mandelbrotGrid

#  = −0.8 + 0.156i
grid = getGrid(-0.8, 0.156)
pygame.init()
screen = pygame.display.set_mode((width, height))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.surfarray.blit_array(screen, grid)
    pygame.display.flip()
pygame.quit()
