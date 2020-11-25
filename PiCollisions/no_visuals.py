from time import sleep


class Block():
    def __init__(self, length, mass, velocity, left):
        self.length = length
        self.mass = mass
        self.velocity = velocity
        self.left = left
        self.right = left + length

    def update(self, dt):
        self.left += self.velocity * dt
        self.right = self.left + self.length
    
    def switchDir(self):
        self.velocity = -1 * self.velocity
        
    @staticmethod
    def collision(block1, block2):
        m1, v10, m2, v20 = block1.mass, block1.velocity, block2.mass, block2.velocity
        block1.velocity = (m1*v10+m2*v20-m2*v10+m2*v20)/(m1+m2)
        block2.velocity = (m1*v10+m2*v20-m1*v20+m1*v10)/(m1+m2)

class Sim():
    def __init__(self, digits):
        self.dim = 1400, 800
        self.left = 10
        self.bot = self.dim[1] - 10
        self.collisions = 0
        self.block1 = Block(50, 1, 0, self.dim[0]*(1/3))
        self.block2 = Block(100, 100 ** (digits - 1), -30, self.dim[0]*(2/3))

    def run(self):
        dt = 0.01
        running = True
        while running:
            self.advance(dt)
            self.handleCollisions()
            if (self.block1.velocity > 0 and self.block2.velocity > 0 and self.block1.velocity < self.block2.velocity):
                break
        print(self.collisions)

    def advance(self, dt):
        self.block1.update(dt)
        self.block2.update(dt)
        
    def handleCollisions(self):
        collision = False
        if self.block1.left < self.left:
            distError = self.block1.left - self.left
            timeError = distError / self.block1.velocity
            self.advance(-timeError)
            self.block1.switchDir()
            collision = True
        elif self.block1.right > self.block2.left:
            timeError = (self.block1.right-self.block2.left)/(self.block1.velocity-self.block2.velocity)
            self.advance(-timeError)
            Block.collision(self.block1, self.block2)
            collision = True
        if collision:
            self.collisions += 1

sim = Sim(3)
sim.run()
