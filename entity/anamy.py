from entity.entity import Entity
from entity.player import Player

class Anamy(Entity):
    def __init__(self, x = 0, y = 0, rad = 0, hp = 100, v = 300):
        super().__init__(x, y, rad, hp)
        self.v = v
        self.dx = 0
        self.dy = 0

    def count_way(self, player: Player):
        dx = player.x - self.x
        dy = player.y - self.y
        if dx:
            self.dx = dx // abs(dx)
        if dy:
            self.dy = dy // abs(dy)

    def update(self, dt, screen_width, screen_height):
        self.x += self.dx * self.v * dt
        self.y += self.dy * self.v * dt

        self.x = max(self.rad, min(screen_width - self.rad, self.x))
        self.y = max(self.rad, min(screen_height - self.rad, self.y))