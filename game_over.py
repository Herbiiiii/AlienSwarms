import pygame
import sys

def game_over(screen):
    """
    Отображает экран окончания игры
    """
    game_over_font = pygame.font.Font(None, 80)
    game_over_text = game_over_font.render("Game Over", True, (255, 0, 0))
    game_over_rect = game_over_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return

        screen.fill((0, 0, 0))
        screen.blit(game_over_text, game_over_rect)
        pygame.display.flip()
