string = """
def mandelbrot(a, b, iters, bound):\noriginalA = a\n
    originalB = b\n
    for i in range(iters):
        aTemp = a**2 - b**2 + originalA
        b = 2 * a * b + originalB
        a = aTemp
        if (a**2 + b**2 >= bound):
            return i
    return iters
"""

import pyautogui

pyautogui.write(string, interval=0.05)