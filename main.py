import pygame
import math


class Body:
    def __init__(self, x, y, vx, vy, mass, color, radius):
        self.x = x
        self.y = y
        self.vy = vy
        self.vx = vx
        self.mass = mass
        self.color = color
        self.radius = radius
        self.trace = []

    def draw(self, win):
        x = self.x * SCALE + WIDTH / 2
        y = self.y * SCALE + HEIGHT / 2

        if len(self.trace) > 2:
            traceLine = []
            for point in self.trace:
                x,y = point
                x = x * SCALE + WIDTH / 2
                y = y * SCALE + HEIGHT / 2
                traceLine.append((x,y))
            pygame.draw.lines(win, self.color, False, traceLine, 2)

        pygame.draw.circle(win, self.color, (x, y), self.radius)

    def attraction(self, other):
        distance_x = other.x - self.x
        distance_y = other.y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        force = G * self.mass * other.mass / distance**2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y

    def updatePosition(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.vx += total_fx / self.mass * TIMESTEP
        self.vy += total_fy / self.mass * TIMESTEP

        self.x += self.vx * TIMESTEP
        self.y += self.vy * TIMESTEP
        self.trace.append((self.x, self.y))


PI = 3.14159265358979323
AU = 149.6e6 * 1000
G = 6.67428e-11
TIMESTEP = 3600*24

SCALE = 250 / AU

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255,255)


def main(ref='sun'):
    pygame.init()
    run = True
    clock = pygame.time.Clock()

    win = pygame.display.set_mode((WIDTH, HEIGHT))
    background = (33, 33,33)
    pygame.display.set_caption("Simulador de Gravidade")

    sun = Body(0, 0,0,0,1.98892 * 10**30,WHITE,50)

    # position = AU
    # vel = m/s
    # mass = kg

    earth = Body(-1 * AU, 0,0,29.783 * 1000,5.9742 * 10**24,WHITE,10)
    mars = Body(-1.524 * AU, 0,0,24.077 * 1000, 6.39 * 10**23,WHITE,10)
    mercury = Body(0.387 * AU, 0,0,-47.4 * 1000,3.30 * 10**23,WHITE,10)
    venus = Body(0.723 * AU, 0,0,-35.02 * 1000,4.8685 * 10**24,WHITE,10)

    bodies = [sun, earth,mars,mercury,venus]

    while run:
        # Roda 60 vezes por segundo
        clock.tick(60)
        # Background da janela
        win.fill(background)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for body in bodies:
            body.updatePosition(bodies)
            body.draw(win)

        # Update gráfico
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
