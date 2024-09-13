import pygame
from random import randint


CAPTION = 'Турбо-мяч'
ICON = pygame.image.load('images/fast-icon.png')
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


pygame.display.set_caption(CAPTION)
pygame.display.set_icon(ICON)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
target_image = pygame.image.load('images/primary_ball.png')
backround_image = pygame.image.load('images/background.png')
target_width = 128
target_height = 128

target_x = randint(0, SCREEN_WIDTH - target_width)
target_y = randint(0, SCREEN_HEIGHT - target_height)

screen.blit(backround_image, (0, 0))

pygame.display.flip()