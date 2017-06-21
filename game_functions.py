import pygame
import sys

def check_events(snake):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, snake)

def check_keydown_events(event, snake):
    """Respond to keypress."""
    if event.key == pygame.K_RIGHT:
        snake.moving_right = True
        snake.moving_left = snake.moveing_down = snake.moving_up = False
    elif event.key == pygame.K_LEFT:
        snake.moving_left = True
        snake.moving_right = snake.moveing_down = snake.moving_up = False
    elif event.key == pygame.K_DOWN:
        snake.moving_down = True
        snake.moving_right = snake.moveing_left = snake.moving_up = False
    elif event.key == pygame.K_UP:
        snake.moving_up = True
        snake.moving_right = snake.moveing_down = snake.moving_left = False
    elif event.key == pygame.K_s:
        snake.moving_down = snake.moving_right = snake.moveing_left = \
            snake.moving_up = False
    elif event.key == pygame.K_q:
        sys.exit()


def update_screen(ai_settings, screen, snake):
    """Update thescreen constantly"""

    # Redraw the screen during each loop. Make sure this is first
    screen.fill(ai_settings.black)

    # Draw the snake
    snake.blitme()

    # Make the most recently drawn screen visible
    pygame.display.flip() # Really need this for the screen to update