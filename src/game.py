import pygame
from src.player import Player
from src.asteroid import Asteroid

class Game:
    def __init__(self):
        pygame.init()

        self.running = True

        self.screen = pygame.display.set_mode([1028, 720])
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill((255, 255, 255))
        self.background = self.background.convert()

        self.asteroid = Asteroid()
        self.player = Player()
        self.play_time = 0

    def main(self):
        while self.running:
            self.on_update()
            self.on_draw()

    def on_draw(self):
        self.screen.blit(self.background, (0, 0))

        self.asteroid.draw(self.screen)
        self.player.draw(self.screen)

        pygame.display.flip()

    def on_update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

        time = pygame.time.get_ticks()
        delta_t = (time - self.play_time) / 100
        self.play_time = pygame.time.get_ticks()

        self.asteroid.update(delta_t)
        self.player.update(delta_t)
