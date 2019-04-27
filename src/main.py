import pygame

pygame.init()

playtime = 0
running = True

screen = pygame.display.set_mode([1028, 720])
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))
background = background.convert()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    clock = pygame.time.Clock()
    milliseconds = clock.tick(30)
    playtime += milliseconds / 1000.0

    screen.blit(background, (0, 0))

    pygame.display.flip()



