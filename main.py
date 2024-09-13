import pygame
from random import randint

caption = 'Турбо-мяч'
screen_width = 800
screen_height = 500

target_width = 100
target_height = 100

icon_image = pygame.image.load('images/fast_icon.png')
ground_image = pygame.image.load('images/background.png')
pri_target = pygame.image.load('images/primary_ball.png')
sec_target = pygame.image.load('images/secondary_ball.png')

pri_target = pygame.transform.scale(pri_target, (target_width, target_height))
sec_target = pygame.transform.scale(sec_target, (target_width, target_height))

pygame.init()

pygame.display.set_caption(caption)
pygame.display.set_icon(icon_image)
screen = pygame.display.set_mode((screen_width, screen_height))

target_x = randint(0, screen_width - target_width)
target_y = randint(0, screen_height - target_height)

running = True

while running:

    screen.blit(ground_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = randint(0, screen_width - target_width)
                target_y = randint(0, screen_height - target_height)

    screen.blit(pri_target, (target_x, target_y))
    pygame.display.update()

pygame.quit()