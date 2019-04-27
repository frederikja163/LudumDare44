import pygame


class Asteroid:
    def __init__(self):
        self.img = pygame.image.load("res/asteroid_large.png")
        self.x = 0
        self.y = 0
        self.vel_x = 10
        self.vel_y = 10

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def update(self, delta_t):
        self.x += self.vel_x * delta_t
        self.y += self.vel_y * delta_t
