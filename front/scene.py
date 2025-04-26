import pygame
from entity.player import Player
from entity.anamy import Anamy
import random

class Scene:
    def __init__(self, width = 800, height = 600):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.player = Player(width // 2, height // 2, 20, 250)
        self.anamies = [Anamy(100, 100, 10, 300, 100)]
        self.clock = pygame.time.Clock()
        self.score = 0
        self.cnt = 0

    def play(self):
        while self.player.isAlive():
            dt = self.clock.tick(60) / 1000
            if len(self.anamies) == 0:
                self.anamies = [Anamy(random.randint(0, self.width), random.randint(0, self.height), 10, 300, 100) for _ in range(2 ** self.cnt)]

            for anamy in self.anamies:
                if not anamy.isAlive():
                    self.anamies.remove(anamy)
                    self.score += 10
                    self.cnt += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.player.hp = 0

            for anamy in self.anamies:
                anamy.count_way(self.player)
                anamy.update(dt, self.width, self.height)
                self.player.handle_input(anamy)

            self.player.update(dt, self.width, self.height)
            self.screen.fill((30, 30, 30))
            for anamy in self.anamies:
                anamy.draw(self.screen)
            self.player.draw(self.screen)
            pygame.display.flip()

        if self.player.isAlive():
            print('You win')
        else:
            print('You lose')
        print('score', self.score)
