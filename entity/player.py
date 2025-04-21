from entity.entity import Entity
import pygame
from math import sqrt

class Player(Entity):
    def __init__(self, x=0, y=0, rad=5, v=300):
        super().__init__(x, y, rad)
        self.v = v
        self.dx = 0
        self.dy = 0

    def handle_input(self, anamy = None, eps = 3):
        keys = pygame.key.get_pressed()

        if not anamy is None and sqrt((anamy.x - self.x) ** 2 + (anamy.y - self.y)**2) - eps <= self.rad + anamy.rad and keys[pygame.K_k]:
            self.attack(anamy)
        self.dx = 0
        self.dy = 0

        if keys[pygame.K_w] or keys[pygame.K_UP]: self.dy = -1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]: self.dy = 1
        if keys[pygame.K_a] or keys[pygame.K_LEFT]: self.dx = -1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]: self.dx = 1