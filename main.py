import pygame


CAPTION = "Турбо-мяч"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.display.set_caption("Турбо-мяч")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
icon = pygame.image.load("fast-icon.png")