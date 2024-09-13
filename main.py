import pygame
from random import randint

CAPTION = 'Турбо-мяч'
ICON = pygame.image.load('images/fast_icon.png')
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

pygame.init()

pygame.display.set_caption(CAPTION)
pygame.display.set_icon(ICON)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
target_image = pygame.image.load('images/primary_ball.png')
backround_image = pygame.image.load('images/background.png')
target_width = 128
target_height = 128

running = True
while running:

    screen.blit(backround_image, (0, 0))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

target_x = randint(0, SCREEN_WIDTH - target_width)
target_y = randint(0, SCREEN_HEIGHT - target_height)

pygame.quit()