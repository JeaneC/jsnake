import pygame

from settings import Settings
from game_stats import GameStats
from snake import Snake
from snake_food import SnakeFood
from pygame.sprite import Group
from scoreboard import Scoreboard

import game_functions as gf

def run_game():

    # Initialize pygame, settings, stats and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("JSnake")

    # Stats
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # Prototype Snake
    snakeHead = Snake(ai_settings, screen, stats)

    # Group of the snake parts
    snake = Group()
    snake.add(snakeHead) # Add the head as the first element

    # Create a list of the snake parts
    snakeBody = [snakeHead]

    # Make a group of snake food
    food = Group()
    snake_food = SnakeFood(ai_settings, screen, stats, snake)
    food.add(snake_food)

    while True:
        gf.check_events(snake, snakeHead)
        if stats.game_active:
            snake.update()
            gf.check_snakeHead_food_collisons(ai_settings, stats, sb,
                                              screen, snakeHead, snake, snakeBody,
                                              food)
            gf.spawn_food(ai_settings, screen, stats,  snake, food)
        gf.update_screen(ai_settings, screen, sb, snake, food)



run_game()