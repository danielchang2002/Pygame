import pyautogui

class Solver:
    def __init__(self, board):
        self.board = board

    def move(self):
        for row in self.board.getBoard():
            for piece in row:
                if not piece.getClicked():
                    continue
                around = piece.getNumAround()
                unknown = 0
                flagged = 0
                neighbors = piece.getNeighbors()
                for p in neighbors:
                    if not p.getClicked():
                        unknown += 1
                    if p.getFlagged():
                        flagged += 1
                if around == flagged:
                    self.openUnflagged(neighbors)
                if around == unknown:
                    self.flagAll(neighbors)

    def openUnflagged(self, neighbors):
        for piece in neighbors:
            if not piece.getFlagged():
                self.board.handleClick(piece, False)


    def flagAll(self, neighbors):
        for piece in neighbors:
            if not piece.getFlagged():
                self.board.handleClick(piece, True)