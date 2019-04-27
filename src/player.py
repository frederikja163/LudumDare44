import pygame


class Player:
    def __init__(self):
        self.player = pygame.image.load("res/player.png")

    def draw(self, screen):
        screen.blit(self.player, (0, 0))

    def update(self):
        pass
