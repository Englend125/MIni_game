import pygame

from entity.anamy import Anamy
from entity.player import *
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
player = Player(width // 2, height // 2, 20)
anamy = Anamy(100, 100, 10, 100, 100)

while player.isAlive() and anamy.isAlive():
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            player.hp = 0

    player.handle_input(anamy)
    player.update(dt, width, height)

    anamy.count_way(player)
    anamy.update(dt, width, height)

    screen.fill((30, 30, 30))
    player.draw(screen)
    anamy.draw(screen)
    pygame.display.flip()

pygame.quit()