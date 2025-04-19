import pygame
from entity.player import Player

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
player = Player(width // 2, height // 2, 20)

running = True
while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.handle_input()
    player.update(dt, width, height)

    screen.fill((30, 30, 30))
    player.draw(screen)
    pygame.display.flip()

pygame.quit()