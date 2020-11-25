class Board:
    def __init__(self, size: tuple):
        self.size = size
        self.board = [[False * 10] * 10]
        print(self.board)

    def print(self):
        for r in self.board:
            for c in r:
                print(c, end="")
            print()


b = Board((5, 5))
b.print()
print('hi')
