import pygame
from src.asteroid import Asteroid


class Game:
    def __init__(self):
        pygame.init()

        self.playtime = 0
        self.running = True

        self.screen = pygame.display.set_mode([1028, 720])
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill((255, 255, 255))
        self.background = self.background.convert()

    def main(self):
        while self.running:
            self.on_update()
            self.on_draw()

    def on_draw(self):
        self.screen.blit(self.background, (0, 0))

        pygame.display.flip()

    def on_update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

        clock = pygame.time.Clock()
        milliseconds = clock.tick(30)
        self.playtime += milliseconds / 1000.0
