import pygame

caption = 'Турбо-мяч'
screen_width = 800
screen_height = 500

target_width = 80
target_height = 80

icon_image = pygame.image.load('images/fast_icon.png')
ground_image = pygame.image.load('images/background.png')
pri_target = pygame.image.load('images/primary_ball.png')
sec_target = pygame.image.load('images/secondary_ball.png')
pri_active = pygame.image.load('images/pri_active.png')
sec_active = pygame.image.load('images/sec_active.png')

pri_target = pygame.transform.scale(pri_target, (target_width, target_height))
sec_target = pygame.transform.scale(sec_target, (target_width, target_height))
pri_active = pygame.transform.scale(pri_active, (target_width, target_height))
sec_active = pygame.transform.scale(sec_active, (target_width, target_height))

pygame.init()

pygame.display.set_caption(caption)
pygame.display.set_icon(icon_image)
screen = pygame.display.set_mode((screen_width, screen_height))

# Начальное положение мяча
target_x = (screen_width - target_width) // 2
target_y = (screen_height - target_height) // 2

# Скорости перемещения по осям и скорость вращения
target_speed_x = 3
target_speed_y = 3
target_speed_r = 8
target_angle = 0

# Показ фона
screen.blit(ground_image, (0, 0))
pygame.display.flip()

# Основной цикл
running = True

active_time = None

pri_image = pri_target
pri_rect = pri_image.get_rect()
sec_image = sec_target
sec_rect = pri_image.get_rect()
active_image = False

switch_ball = 1

clock = pygame.time.Clock()

while running:

    screen.blit(ground_image, (0, 0))
    target_activate = False
    activate_time = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_bound = target_x + target_width
            y_bound = target_y + target_height
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < x_bound and target_y < mouse_y < y_bound:
                active_image = True
                pri_image = pri_active
                active_time = pygame.time.get_ticks()
                print('Попал')
            else:
                print('Промах')

    if active_image and (pygame.time.get_ticks() - active_time >= 250):
        active_image = False
        pri_image = pri_target

    # Изменение положения мяча
    target_x += target_speed_x
    target_y += target_speed_y

    # Изменение угла вращения
    target_angle = (target_angle + target_speed_r) % 360

    # Проверка столкновения с краями окна и изменение направления
    if target_x <= 0 or target_x + target_width >= screen_width:
        target_speed_x = -target_speed_x
        switch_ball *= -1

    if target_y <= 0 or target_y + target_height >= screen_height:
        target_speed_y = -target_speed_y
        switch_ball *= -1

    # Отрисовка мяча
    if switch_ball == 1:
        pri_rotated = pygame.transform.rotate(pri_image, target_angle)
        pri_act_rotated = pygame.transform.rotate(pri_active, target_angle)
        new_rectangle = pri_rotated.get_rect(center=(target_x + target_width // 2, target_y + target_height // 2))
        screen.blit(pri_rotated, new_rectangle.topleft)

    else:
        sec_rotated = pygame.transform.rotate(sec_target, target_angle)
        sec_act_rotated = pygame.transform.rotate(sec_active, target_angle)
        new_rectangle = sec_rotated.get_rect(center=(target_x + target_width // 2, target_y + target_height // 2))
        screen.blit(sec_rotated, new_rectangle.topleft)

    # Обновление части экрана под мячом
    update_rectangle = pygame.Rect(target_x - 20, target_y - 20, target_width + 40, target_height + 40)
    pygame.display.update(update_rectangle)

    # Ограничение FPS
    pygame.time.Clock().tick(30)

pygame.quit()