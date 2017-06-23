import pygame
import game_functions as gf

from settings import Settings
from game_stats import GameStats
from snake import Snake
from pygame.sprite import Group
from scoreboard import Scoreboard



def run_game():

    # Initialize pygame, settings, stats and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("JSnake")

    # Statsx
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Snake head
    snakeHead = Snake(ai_settings, screen, stats)
    snakeHead.head = True

    # Group of the snake parts
    snakes = Group()
    snakes.add(snakeHead) # Add the head as the first element
    snakeBody = [snakeHead] # Create a list of the snake parts

    # Make a group of snake food
    food = Group()

    # Make mouse invisible
    pygame.mouse.set_visible(False)

    while True:
        gf.check_events(ai_settings, screen, stats, snakes, snakeHead)
        if stats.game_active:
            snakes.update()
            gf.check_snakeHead_food_collisions(ai_settings, stats, sb,
                                              screen, snakeHead, snakes, snakeBody,
                                              food)
            gf.spawn_food(ai_settings, screen, stats,  snakes, food)
            gf.check_snake_bottom(screen, stats, snakeHead)
            gf.check_snake_collisions(stats, snakeHead, snakes)
            gf.update_snake(ai_settings, stats, screen, snakes, food)
        gf.update_screen(ai_settings, screen, sb, snakes, food, snakeHead)




run_game()