import pygame
class progress_bar:
    def __init__(self, num = 100, width = 50, high = 5):
        self.width = width
        self.high = high
        self.num = num
        self.cur = num

    def update(self, d):
        if d < 0:
            cur = max(0, self.cur - d)
        else:
            cur = min(self.num, self.cur + d)

    def draw(self, screen: pygame.display, x, y):
        pygame.draw.rect(screen, 'white', x - self.high, )
