import sys
from game import Game

def main():
    size = int(sys.argv[1]), int(sys.argv[2])
    prob = float(sys.argv[3])
    g = Game(size, prob)
    g.run()

if __name__ == '__main__':
    main()