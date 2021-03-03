import pygame

class Block:
    def __init__(self, x, y, color):
        self.x, self.y = x, y
        self.color = color
    
    def equals(self, other):
        return other.x == self.x and other.y == self.y