import pygame


class Player:
    def __init__(self):
        self.player = pygame.image.load("res/player.png")

        self.x = 0
        self.y = 0

        self.speed = 0.2

    def draw(self, screen):
        screen.blit(self.player, (self.x, self.y))

    def update(self, delta_t):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.y += 1 * delta_t * self.speed
        if keys[pygame.K_a]:
            self.x -= 1 * delta_t * self.speed
        if keys[pygame.K_d]:
            self.x += 1 * delta_t * self.speed
