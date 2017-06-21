import pygame
from settings import Settings
from game_stats import GameStats
from snake import Snake
import game_functions as gf

def run_game():

    # Initialize pygame, settings, stats and screen object.
    pygame.init()
    ai_settings = Settings()
    stats = GameStats(ai_settings)
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("JSnake")

    # Prototype Snake 1
    snake = Snake(ai_settings, screen)

    while True:
        gf.check_events(snake)
        if stats.game_active:
            snake.update()
        gf.update_screen(ai_settings, screen, snake)




run_game()