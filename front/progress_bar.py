import pygame
class progress_bar:
    def __init__(self, num = 100, width = 50, height = 5):
        self.width = width
        self.height = height
        self.num = num
        self.cur = num

    def update(self, d):
        self.cur = max(0, self.cur - d)

    def draw(self, screen: pygame.display, x, y, rad):
        pygame.draw.rect(screen,'white', (x - self.width // 2, y - self.height - rad, self.width, self.height))
        pygame.draw.rect(screen,'red', (x - self.width // 2, y - self.height - rad, self.width * (self.cur / self.num), self.height))
