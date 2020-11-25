import pygame
import math
import random
import time

class LSystem:
    def __init__(self, axiom, rules, x, y, length, dtheta):
        self.axiom = axiom
        self.sentence = axiom
        self.rules = rules
        self.xInit = x
        self.yInit = y
        self.x = x
        self.y = y
        self.theta = math.pi / 2
        self.length = length
        self.dtheta = dtheta
        self.stack = []

    def generate(self):
        self.x = self.xInit
        self.y = self.yInit
        self.theta = math.pi / 2
        self.length *= 0.75
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
        color = 0
        dcolor = 255 / len(self.sentence)
        for char in self.sentence:
            # print(char)
            if (char == 'F' or char == 'G' or char == 'A' or char == 'B'):
                x2 = self.x - self.length * math.cos(self.theta)
                y2 = self.y - self.length * math.sin(self.theta)
                pygame.draw.line(screen, (color, 255 - color, 100 + color / 255, 100),
                                 (self.x, self.y), (x2, y2))
                self.x = x2
                self.y = y2
            elif (char == '+'):
                self.theta += self.dtheta
            elif (char == '-'):
                self.theta -= self.dtheta
            elif (char == '['):
                self.stack.append(
                    {'x': self.x, 'y': self.y, 'theta': self.theta})
            elif (char == ']'):
                dict = self.stack.pop()
                self.x = dict['x']
                self.y = dict['y']
                self.theta = dict['theta']
            color += dcolor
