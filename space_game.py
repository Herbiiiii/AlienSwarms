import pygame
import sys
from pygame.sprite import Group
from stats import Stats
from scores import Scores
from gun import Gun
import controls
import game_over

def run(): #запуск игры
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Space tank")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controls.update(bg_color, screen, stats, sc, gun, inos, bullets)
            controls.update_bullets(screen, stats, sc, inos, bullets)
            controls.update_inos(stats, screen, sc, gun, inos, bullets)
        else:
            game_over.game_over(screen)


# Инициализация Pygame
pygame.init()

# Размеры экрана
screen_width = 700
screen_height = 800

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
RED = (255, 0, 0)

# Создание экрана
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Tank")

# Параметры меню
menu_font = pygame.font.Font(None, 60)
menu_selected_font = pygame.font.Font(None, 80)
menu_padding = 40

# Параметры загрузочного экрана
loading_font = pygame.font.Font(None, 40)
loading_text = loading_font.render("Space Tank", True, WHITE)
loading_rect = loading_text.get_rect(center=(screen_width // 2, screen_height // 2))
continue_text = loading_font.render("LOADING", True, WHITE)
continue_rect = continue_text.get_rect(center=(screen_width // 2, screen_height // 2 + 50))

#rules
rules_text = "A - движение влево, D - движение вправо, Space - стрельба"
rules_font = pygame.font.Font(None, 30)
rules_text_rendered = rules_font.render(rules_text, True, WHITE)
rules_rect = rules_text_rendered.get_rect(center=(screen_width // 2, screen_height // 2))

# Переменные меню
loading_active = True #Инициализация загрузочного экрана
menu_active = False #Инициализация меню
rules_active = False #Инициализация правил
about_active = False #Инициализация об авторе
menu_selected_item = 0

def draw_about():
    screen.fill(BLACK)

    # Рисуем заголовок окна «О программе»
    title_text = menu_font.render("About", True, WHITE)
    title_rect = title_text.get_rect(center=(screen_width // 2, 150))
    screen.blit(title_text, title_rect)
    # Нарисовать информацию об авторе
    author_text = menu_font.render("Бондарев С.А. БСБО-11-21", True, WHITE)
    author_rect = author_text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(author_text, author_rect)

    pygame.display.flip()

def draw_loading_screen():
    screen.fill(BLACK)

    # Отрисовка названия игры
    game_title_font = pygame.font.Font(None, 90)
    game_title_text = game_title_font.render("Space Tank", True, WHITE)
    game_title_rect = game_title_text.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
    screen.blit(game_title_text, game_title_rect)

    # Отрисовка надписи "LOADING"
    continue_font = pygame.font.Font(None, 40)
    continue_text = continue_font.render("LOADING", True, GRAY)
    continue_rect = continue_text.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
    screen.blit(continue_text, continue_rect)

    pygame.display.flip()

def draw_menu():
    screen.fill(BLACK)

    # Отрисовка заголовка меню
    title_text = menu_font.render("Main Menu", True, WHITE)
    title_rect = title_text.get_rect(center=(screen_width // 2, 150))
    screen.blit(title_text, title_rect)

    # Отрисовка пунктов меню
    items = ["Start Game", "Rules", "About", "Quit"]
    for i, item in enumerate(items):
        if i == menu_selected_item:
            item_text = menu_selected_font.render(item, True, RED)
        else:
            item_text = menu_font.render(item, True, WHITE)
        item_rect = item_text.get_rect(center=(screen_width // 2, 300 + i * (menu_padding + item_text.get_height())))
        screen.blit(item_text, item_rect)

    pygame.display.flip()

def draw_rules():
    screen.fill(BLACK)

    # Рисуем заголовок окна правил
    title_text = menu_font.render("Rules", True, WHITE)
    title_rect = title_text.get_rect(center=(screen_width // 2, 150))
    screen.blit(title_text, title_rect)

    # Нарисуйте текст с правилами игры
    screen.blit(rules_text_rendered, rules_rect)

    pygame.display.flip()

# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if loading_active:
                loading_active = False
            elif menu_active:
                if event.key == pygame.K_UP:
                    menu_selected_item = (menu_selected_item - 1) % 4
                elif event.key == pygame.K_DOWN:
                    menu_selected_item = (menu_selected_item + 1) % 4
                elif event.key == pygame.K_RETURN:
                    if menu_selected_item == 0:
                        menu_active = False
                        pygame.mouse.set_visible(False)
                    elif menu_selected_item == 1:
                        menu_active = False
                        rules_active = True
                        draw_rules()
                    elif menu_selected_item == 2:
                        menu_active = False
                        about_active = True
                        draw_about()
                    elif menu_selected_item == 3:
                        pygame.quit()
                        sys.exit()
                elif event.key == pygame.K_ESCAPE:
                    rules_active = False
                    menu_active = True
                    draw_menu()
                elif event.key == pygame.K_RETURN:
                    about_active = False
                    menu_active = True
                    draw_menu()
            else:
                run()

    if loading_active:
        draw_loading_screen()
        pygame.time.wait(2000)
        loading_active = False
        menu_active = True
    elif menu_active:
        draw_menu()
    elif rules_active:
        draw_rules()
    elif about_active:
        draw_about()
    else:
        run()



