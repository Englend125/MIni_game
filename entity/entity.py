import pygame

class Entity:
    def __init__(self, x = 0, y = 0, rad = 5, hp = 100, v = 300):
        self.x = x
        self.y = y
        self.rad = rad
        self.hp = hp
        self.v = v
        self.dx = 0
        self.dy = 0

    def goto(self, x, y):
        self.x = x
        self.y = y

    def resize(self, rad):
        if rad > 0:
            self.rad = rad

    def getPos(self):
        return [self.x, self.y]

    def draw(self, screen:pygame.display):
        pygame.draw.circle(screen, 'white', self.getPos(), self.rad)

    def update(self, dt, screen_width, screen_height):
        self.x += self.dx * self.v * dt
        self.y += self.dy * self.v * dt

        self.x = max(self.rad, min(screen_width - self.rad, self.x))
        self.y = max(self.rad, min(screen_height - self.rad, self.y))