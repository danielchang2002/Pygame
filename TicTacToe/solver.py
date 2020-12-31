from math import inf

class Solver():
    def getBestMove(self, board, maximizer):
        maxScore = -1 * inf
        bestBoard = None
        self.maximizer = maximizer
        self.minimizer = 'X' if maximizer == 'O' else 'O'
        for b in board.getNeighbors(maximizer):
            score = self.getScore(b, False, 0)
            if (score > maxScore):
                maxScore = score
                bestBoard = b
        return bestBoard
    
    def getScore(self, board, isMaximizer, move):
        if (board.getHasWon(self.maximizer)):
            return 10 - move
        elif (board.getHasWon(self.minimizer)):
            return -10 + move
        elif (board.isFull()):
            return 0

        if (isMaximizer):
            bestScore = -1 * inf
            for b in board.getNeighbors(self.maximizer):
                score = self.getScore(b, False, move + 1)
                bestScore = max(bestScore, score)
            return bestScore
        else:
            bestScore = inf
            for b in board.getNeighbors(self.minimizer):
                score = self.getScore(b, True, move + 1)
                bestScore = min(bestScore, score)
            return bestScore

