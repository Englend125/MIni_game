from entity.entity import Entity
from entity.player import Player
from math import sqrt

class Anamy(Entity):
    def __init__(self, x = 0, y = 0, rad = 0, hp = 100, v = 300):
        super().__init__(x, y, rad, hp)
        self.v = v
        self.dx = 0
        self.dy = 0

    def count_way(self, player: Player):
        dx = player.x - self.x
        dy = player.y - self.y
        if sqrt(dx**2 + dy**2) <= self.rad + player.rad:
            self.dx = 0
            self.dy = 0
            return
        if dx:
            self.dx = dx // abs(dx)
        if dy:
            self.dy = dy // abs(dy)