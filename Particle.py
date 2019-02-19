import pygame, Vector

class Particle():
    def __init__(self, x, y, xvel, yvel, radius, color, surface):
        self.pos = Vector.Vector(x, y)
        self.vel = Vector.Vector(xvel, yvel)
        self.acc = Vector.Vector(0, 0)
        self.radius = radius
        self.color = color
        self.surface = surface

    def draw(self):
        pygame.draw.circle(self.surface, self.color, (int(self.pos.x), int(self.pos.y)), self.radius)

    def update(self):
          self.vel.add(self.acc)
