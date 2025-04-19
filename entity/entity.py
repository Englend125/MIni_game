import pygame

class Entity:
    def __init__(self, x = 0, y = 0, rad = 5, hp = 100):
        self.x = x
        self.y = y
        self.rad = rad
        self.hp = hp

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