from entity.entity import Entity
import pygame

class Player(Entity):
    def __init__(self, x=0, y=0, rad=5, v=300):
        super().__init__(x, y, rad)
        self.v = v
        self.dx = 0
        self.dy = 0

    def handle_input(self):
        keys = pygame.key.get_pressed()
        self.dx = 0
        self.dy = 0

        if keys[pygame.K_w]: self.dy = -1
        if keys[pygame.K_s]: self.dy = 1
        if keys[pygame.K_a]: self.dx = -1
        if keys[pygame.K_d]: self.dx = 1