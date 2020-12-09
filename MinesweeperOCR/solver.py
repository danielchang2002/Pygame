import pyautogui
import numpy as np  
from time import sleep
import keyboard
from board import Board
import os
pyautogui.FAILSAFE = True

class Solver:
    def __init__(self, size):
        self.size = size
        self.board = Board(size)
        self.setRegion()
        self.pieceSize = self.region[2] / size[1], self.region[3] / size[0]
        self.setColors()
        self.setBoard()

    def setColors(self):
        self.colors = np.zeros([7, 3])
        with open ('rgb.txt') as f:
            for i in range(7):
                line = f.readline()
                self.colors[i, :] = [int(i) for i in line.split()]

    def setRegion(self):
        keyboard.wait('esc')
        x1, y1 = pyautogui.position()
        keyboard.wait('esc')
        x2, y2 = pyautogui.position()
        self.region = (2 * x1, 2 * y1, 2 * (x2 - x1), 2 * (y2 - y1))

    def setBoard(self):
        screenshot = pyautogui.screenshot("s.png", region=self.region)
        center = self.region[2] / self.size[1], self.region[3] / self.size[0]
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                number = self.getNumber(screenshot, center)
                print(row, col, number)
                
    def getNumber(self, screenshot, center):
        threshold = 10
        for x in range(int(center[0] - 5), int(center[0] + 5)):
            rgb = np.asarray(screenshot.getpixel((x, center[1]))[:3])
            print(rgb)
            dif = np.sum(np.square(rgb - self.colors), 1)
            if (np.amin(dif) < threshold):
                return np.argmin(dif)
        return 0