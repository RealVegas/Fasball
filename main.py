import pygame

running = True

while running:

    screen.blit(ground-image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()