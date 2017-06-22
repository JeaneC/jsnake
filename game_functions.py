import pygame
import sys

from snake_food import SnakeFood

def check_events(snakeHead):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, snakeHead)

def check_keydown_events(event, snakeHead):
    """Respond to keypress."""
    if event.key == pygame.K_RIGHT:
        snakeHead.moving_right = True
        snakeHead.moving_left = snakeHead.moveing_down = snakeHead.moving_up = False
    elif event.key == pygame.K_LEFT:
        snakeHead.moving_left = True
        snakeHead.moving_right = snakeHead.moveing_down = snakeHead.moving_up = False
    elif event.key == pygame.K_DOWN:
        snakeHead.moving_down = True
        snakeHead.moving_right = snakeHead.moveing_left = snakeHead.moving_up = False
    elif event.key == pygame.K_UP:
        snakeHead.moving_up = True
        snakeHead.moving_right = snakeHead.moveing_down = snakeHead.moving_left = False
    elif event.key == pygame.K_s:
        snakeHead.moving_down = snakeHead.moving_right = snakeHead.moveing_left = \
            snakeHead.moving_up = False
    elif event.key == pygame.K_q:
        sys.exit()

def check_snakeHead_food_collisons(ai_settings, stats, sb, screen,
                                   snakeHead, snake, food):
    """Check to see if the head of the snake bumpeed into food"""


    if pygame.sprite.spritecollideany(snakeHead, food):
        foodPart = pygame.sprite.spritecollideany(snakeHead, food)
        foodPart.remove(food)
        ## foodPart.add(snake)
        stats.score += 1
        ## print(stats.score)
        sb.prep_score()
    check_high_score(stats, sb)

def check_high_score(stats, sb):
    """Check high score"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

def spawn_food(ai_settings, screen, snake, food):

    if(len(food) < 2): # So far this works
        snake_food = SnakeFood(ai_settings, screen, snake)
        food.add(snake_food)


def update_screen(ai_settings, screen, sb, snake, food):
    """Update thescreen constantly"""

    # Redraw the screen during each loop. Make sure this is first
    screen.fill(ai_settings.black)

    # Draw the score
    sb.show_score()

    # Draw the snake
    for snake_piece in snake.sprites():
        snake_piece.blitme()

    # Draw the snake food
    for snake_food in food.sprites():
        snake_food.blitme()

    # Make the most recently drawn screen visible
    pygame.display.flip() # Really need this for the screen to update

    # check_snakeHead_food_collisions

