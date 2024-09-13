import pygame

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

target_x = (screen_width - target_width) // 2
target_y = (screen_height - target_height) // 2
target_speed_x = 5
target_speed_y = 5
angle = 0
rotation_speed = 5

screen.blit(ground_image, (0, 0))
pygame.display.flip()

running = True
while running:

    screen.blit(ground_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Изменение позиции мяча
    target_x += target_speed_x
    target_y += target_speed_y

    # Обновление угла вращения
    angle = (angle + rotation_speed) % 360

    # Проверка столкновения с краями окна и изменение направления
    if target_x <= 0 or target_x + target_width >= screen_width:
         target_speed_x = -target_speed_x
    if target_y <= 0 or target_y + target_height >= screen_height:
         target_speed_y = -target_speed_y

    if target_speed_x > 0 and target_speed_y > 0:
        screen.blit(pri_target, (target_x, target_y))

    elif target_speed_x > 0 and target_speed_y < 0:
        screen.blit(pri_target, (target_x, target_y))

    elif target_speed_x < 0 and target_speed_y < 0:
        rotated_sec = pygame.transform.rotate(sec_target, angle)
        new_rect = rotated_sec.get_rect(center=(target_x + target_width // 2, target_y + target_height // 2))
        screen.blit(rotated_sec, new_rect.topleft)

    elif target_speed_x < 0 and target_speed_y > 0:
        rotated_sec = pygame.transform.rotate(sec_target, angle)
        new_rect = rotated_sec.get_rect(center=(target_x + target_width // 2, target_y + target_height // 2))
        screen.blit(rotated_sec, new_rect.topleft)

    # Обновление части
    rect = pygame.Rect(target_x - 10, target_y - 10, target_width + 20, target_height + 20)
    pygame.display.update(rect)

    # Ограничение FPS
    pygame.time.Clock().tick(60)

pygame.quit()

# if event.type == pygame.MOUSEBUTTONDOWN:
#     mouse_x, mouse_y = pygame.mouse.get_pos()
#     if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
#         target_x = randint(0, screen_width - target_width)
#         target_y = randint(0, screen_height - target_height)