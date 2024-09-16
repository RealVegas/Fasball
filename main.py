import pygame
import sys

pygame.init()
pygame.font.init()

# Константы для инициализации окна
caption: str = 'Турбо-мяч v 1.0'
screen_width: int = 800
screen_height: int = 500

# Размеры мячей
target_width: int = 80
target_height: int = 80

# Загрузка изображений мячей и фона
icon_image = pygame.image.load('images/fast_icon.png')
ground_image = pygame.image.load('images/background.png')
pri_target = pygame.image.load('images/primary_ball.png')
sec_target = pygame.image.load('images/secondary_ball.png')
pri_active = pygame.image.load('images/pri_active.png')
sec_active = pygame.image.load('images/sec_active.png')

# Изменение размера мячей
pri_target = pygame.transform.scale(pri_target, (target_width, target_height))
sec_target = pygame.transform.scale(sec_target, (target_width, target_height))
pri_active = pygame.transform.scale(pri_active, (target_width, target_height))
sec_active = pygame.transform.scale(sec_active, (target_width, target_height))

# Оформление главного окна
pygame.display.set_caption(caption)
pygame.display.set_icon(icon_image)
screen = pygame.display.set_mode((screen_width, screen_height))

# Начальное положение мяча
target_x: int = (screen_width - target_width) // 2
target_y: int = (screen_height - target_height) // 2

# Скорости перемещения по осям и скорость вращения
target_speed_x: int = 0
target_speed_y: int = 0
target_speed_r: int = 6
target_angle: int = 0

# Переменные для переключения состояния мяча
pri_image = pri_target
pri_rect = pri_image.get_rect()
sec_image = sec_target
sec_rect = pri_image.get_rect()

activate_image: bool = False
activate_time: int = 0

# Переменная для переключения вида мяча
change_ball: int = 1

# Переменные для подсчета очков
user_score: int = 0
miss_scores: int = 0
# Переменная для контроля событий при подсчете очков
events_enabled: bool = True

# Основной цикл
running = True

# Переменные для режима паузы
save_speed_x: int = 0
save_speed_y: int = 0
save_speed_r: int = 0

clock = pygame.time.Clock()
while running:

    screen.blit(ground_image, (0, 0))
    user_count: bool = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Нажатие на клавишу "P"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if save_speed_x == 0 and save_speed_y == 0:
                    save_speed_x, save_speed_y, save_speed_r = target_speed_x, target_speed_y, target_speed_r
                    target_speed_x, target_speed_y = 0, 0
                    target_speed_r = round(target_speed_r / 1.5)

                elif save_speed_x != 0 and save_speed_y != 0:
                    target_speed_x, target_speed_y, target_speed_r = save_speed_x, save_speed_y, save_speed_r
                    save_speed_x, save_speed_y = 0, 0

        # Нажатие на левую кнопу мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            if target_speed_x == 0 and target_speed_y == 0:
                target_speed_x: int = 4
                target_speed_y: int = 4
                target_speed_r: int = round(target_speed_x * 1.5)

            mouse_x, mouse_y = pygame.mouse.get_pos()
            x_bound: int = target_x + target_width
            y_bound: int = target_y + target_height

            if target_x < mouse_x < x_bound and target_y < mouse_y < y_bound:
                if events_enabled:
                    user_score += 1
                    events_enabled: bool = False
                activate_image: bool = True
                activate_time: int = pygame.time.get_ticks()
                pri_image = pri_active
                sec_image = sec_active

    if activate_image and (pygame.time.get_ticks() - activate_time >= 250):
        activate_image: bool = False
        pri_image = pri_target
        sec_image = sec_target

    # Изменение положения мяча
    target_x += target_speed_x
    target_y += target_speed_y

    # Изменение угла вращения
    target_angle: int = (target_angle + target_speed_r) % 360

    # Проверка столкновения с краями окна и изменение направления
    if target_x <= 0 or target_x + target_width >= screen_width:
        change_ball *= -1
        target_speed_x: int = -target_speed_x
        if events_enabled:
            miss_scores += 1
        else:
            events_enabled: bool = True

    if target_y <= 0 or target_y + target_height >= screen_height:
        change_ball *= -1
        target_speed_y: int = -target_speed_y
        if events_enabled:
            miss_scores += 1
        else:
            events_enabled: bool = True

    # Отрисовка текста
    font = pygame.font.Font('fonts/constan.ttf', 64)
    text = font.render(f'попал...{user_score}|{miss_scores}...пропустил', True, (255, 225, 255))  # белый текст
    text_rect = text.get_rect(center=(400, 250))

    screen.blit(text, text_rect)

    # Отрисовка мяча
    pri_rotated = pygame.transform.rotate(pri_image, target_angle)
    sec_rotated = pygame.transform.rotate(sec_image, target_angle)

    new_rectangle = pri_rotated.get_rect(center=(target_x + target_width // 2, target_y + target_height // 2))

    if change_ball == 1:
        screen.blit(pri_rotated, new_rectangle.topleft)
    else:
        screen.blit(sec_rotated, new_rectangle.topleft)

    pygame.display.flip()

    # Обновление части экрана под мячом
    # Из-за текста пришлось отказаться от этого метода
    # update_rectangle = pygame.Rect(target_x - 20, target_y - 20, target_width + 40, target_height + 40)
    # pygame.display.update(update_rectangle)

    # Ограничение FPS
    pygame.time.Clock().tick(80)

pygame.quit()
sys.exit()