import pygame, random, Vector, Particle, Field, math

winWidth, winHeight = 700, 700

pygame.init()
win = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("Simulator")

particles = []
f = Field.Field(0, 0, 700, 700)
for i in range(f.dim.x):
     for j in range(f.dim.y):
          x = i-350
          y = j-350
          dx = y/30
          dy = -(x**2)/2000
          f.setVectors(i, j, Vector.Vector(dx, dy))

for i in range(300):
     p = Particle.Particle(random.randint(300, 400), random.randint(300, 400), 0, 0, 5, (255, 0, 0), win)
     particles.append(p)

running = True
while running:
     pygame.time.delay(10)
     win.fill(0)

     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

     for p in particles:
          if p.pos.x > 600:
               p.pos.x = 100
          if p.pos.x < 100:
               p.pos.x = 600
          if p.pos.y > 600:
               p.pos.y = 100
          if p.pos.y < 100:
               p.pos.y = 600
          p.pos.add(f.getVector(p.pos.x, p.pos.y))
          p.draw()

     pygame.display.update()

pygame.quit()