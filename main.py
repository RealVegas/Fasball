import pygame
from random import randint

caption = 'Турбо-мяч'
screen_width = 800
screen_height = 500

icon_image = pygame.image.load('images/fast_icon.png')
target_image = pygame.image.load('images/primary_ball.png')
background_image = pygame.image.load('images/background.png')

pygame.init()

pygame.display.set_caption(caption)
pygame.display.set_icon(icon_image)
screen = pygame.display.set_mode((screen_width, screen_height))

target_width = 128
target_height = 128

running = True
while running:

    screen.blit(background_image, (0, 0))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

target_x = randint(0, SCREEN_WIDTH - target_width)
target_y = randint(0, SCREEN_HEIGHT - target_height)

pygame.quit()