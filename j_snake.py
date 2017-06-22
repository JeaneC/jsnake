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
    snakeHead = Snake(ai_settings, screen)

    # Group of the snake parts
    snake = Group()
    snakeHeadG = Group()
    snake.add(snakeHead) # Add the head as the first element
    snakeHeadG.add(snakeHead) # Seems redundant, but this is my current fix

    # Make a group of snake food
    food = Group()
    snake_food = SnakeFood(ai_settings, screen, snake)
    food.add(snake_food)

    while True:
        gf.check_events(snakeHead)
        if stats.game_active:
            snake.update()
            gf.check_snakeHead_food_collisons(ai_settings, stats, sb,
                                              screen, snakeHead, snake,
                                              food)
            gf.spawn_food(ai_settings, screen, snake, food)
        gf.update_screen(ai_settings, screen, sb,  snake, food)



run_game()