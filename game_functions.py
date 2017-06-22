import pygame
import sys

from pygame.sprite import Group
from snake_food import SnakeFood
from turnPoint import TurnPoint
from snake import Snake

def check_events(ai_settings, screen, stats, snakes, snakeHead):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(ai_settings, screen, event, stats,
                                 snakes, snakeHead)

def check_keydown_events(ai_settings, screen, event, stats, snakes, snakeHead):
    """Respond to keypress."""
    if snakeHead.lock:
        if event.key == pygame.K_RIGHT:
            if not snakeHead.moving_right and not snakeHead.moving_left:
                snakeHead.moving_right = True
                snakeHead.moving_left = snakeHead.moving_down = snakeHead.moving_up = False
                establish_movePoint(ai_settings, screen, snakeHead, snakes,  1)
        elif event.key == pygame.K_LEFT:
            if not snakeHead.moving_right and not snakeHead.moving_left:
                snakeHead.moving_left = True
                snakeHead.moving_right = snakeHead.moving_down = snakeHead.moving_up = False
                establish_movePoint(ai_settings, screen, snakeHead, snakes, 2)
        elif event.key == pygame.K_DOWN:
            if not snakeHead.moving_down and not snakeHead.moving_up:
                snakeHead.moving_down = True
                snakeHead.moving_right = snakeHead.moving_left = snakeHead.moving_up = False
                establish_movePoint(ai_settings, screen, snakeHead, snakes, 3)
        elif event.key == pygame.K_UP:
            if not snakeHead.moving_down and not snakeHead.moving_up:
                snakeHead.moving_up = True
                snakeHead.moving_right = snakeHead.moving_down = snakeHead.moving_left = False
                establish_movePoint(ai_settings, screen, snakeHead, snakes, 4)
        elif event.key == pygame.K_s:
            snakeHead.moving_down = snakeHead.moving_right = snakeHead.moving_left = \
            snakeHead.moving_up = False
        elif event.key == pygame.K_q:
            sys.exit()

    if not snakeHead.lock:
        if event.key == pygame.K_RIGHT:
            if not snakeHead.moving_right:
                snakeHead.moving_right = True
                snakeHead.moving_left = snakeHead.moving_down = snakeHead.moving_up = False
                establish_movePoint(ai_settings, screen, snakeHead, snakes,  1)
        elif event.key == pygame.K_LEFT:
            if not snakeHead.moving_left:
                snakeHead.moving_left = True
                snakeHead.moving_right = snakeHead.moving_down = snakeHead.moving_up = False
                establish_movePoint(ai_settings, screen, snakeHead, snakes, 2)
        elif event.key == pygame.K_DOWN:
            if not snakeHead.moving_down:
                snakeHead.moving_down = True
                snakeHead.moving_right = snakeHead.moving_left = snakeHead.moving_up = False
                establish_movePoint(ai_settings, screen, snakeHead, snakes, 3)
        elif event.key == pygame.K_UP:
            if not snakeHead.moving_up:
                snakeHead.moving_up = True
                snakeHead.moving_right = snakeHead.moving_down = snakeHead.moving_left = False
                establish_movePoint(ai_settings, screen, snakeHead, snakes, 4)
        elif event.key == pygame.K_s:
            snakeHead.moving_down = snakeHead.moving_right = snakeHead.moving_left = \
            snakeHead.moving_up = False
        elif event.key == pygame.K_q:
            sys.exit()

def establish_movePoint(ai_settings, screen, snakeHead, snakes, direction):
    # print("Happened")
    movePointX = snakeHead.center
    movePointY = snakeHead.y

    new_turnPoint = TurnPoint(ai_settings, screen, movePointX, movePointY, direction)

    for snake in snakes:
        if not snake.head:
            snake.turnPoints.add(new_turnPoint) # Adds only new turn points




def enlarge_snake(ai_settings, screen, stats, snakes, snakeList, snakeColor):

    snake_body = Snake(ai_settings, screen, stats)

    snake_body.color = snakeColor

    snake_body.moving_left = snakeList[-1].moving_left
    snake_body.moving_down = snakeList[-1].moving_down
    snake_body.moving_right = snakeList[-1].moving_right
    snake_body.moving_up = snakeList[-1].moving_up

    snake_body.y = snakeList[-1].y
    snake_body.center = snakeList[-1].center

    for turnPoint in snakeList[-1].turnPoints:
        snake_body.turnPoints.add(turnPoint)

    if (snakeList[-1].moving_up):
        snake_body.y += 25
        if snakeList[-1].head:
            snake_body.y += 15
    elif (snakeList[-1].moving_down):
        snake_body.y -= 25
        if snakeList[-1].head:
            snake_body.y -= 15
    elif (snakeList[-1].moving_left):
        snake_body.center += 25
        if snakeList[-1].head:
            snake_body.center += 15
    elif (snakeList[-1].moving_right):
        snake_body.center -= 25
        if snakeList[-1].head:
            snake_body.center -= 15

    if(stats.score > 0 and stats.score < 3):
        snake_body.head2 = True

    # Add to the group
    snake_body.add(snakes)
    # snakes.add(snake_body) # This doesn't seem to be working
    snakeList.append(snake_body) ## This is working
    print(snakes.sprites())
    snakes.update()

def spawn_food(ai_settings, screen, stats, snake, food):

    if(len(food) < 2): # So far this works
        snake_food = SnakeFood(ai_settings, screen, stats, snake)
        food.add(snake_food)

def check_turning_point(ai_settings, screen, snake, food):
    if not snake.head:
        if pygame.sprite.spritecollideany(snake, snake.turnPoints):
            turnPoint = pygame.sprite.spritecollideany(snake, snake.turnPoints)
            if(snake.center == turnPoint.rect.x and snake.y == turnPoint.rect.y):
                snake.stop()
                snake.moving_left = turnPoint.left
                snake.moving_right = turnPoint.right
                snake.moving_up = turnPoint.up
                snake.moving_down = turnPoint.down

                turnPoint.remove(snake.turnPoints)

def check_snake_bottom(screen, stats, snakeHead):
    """Check to see if the snake is at the bottom"""
    screen_rect = screen.get_rect()

    if(snakeHead.rect.right >= screen_rect.right or
        snakeHead.rect.left <= 0 or
        snakeHead.rect.y <= 0 or
        snakeHead.rect.y >= snakeHead.ai_settings.screen_height - 20):

        stats.game_active = False
        pygame.mouse.set_visible(True)



def update_snake(ai_settings, stats, screen, snakes, food):
    for snake in snakes:
        check_turning_point(ai_settings, screen, snake, food)

def check_snakeHead_food_collisions(ai_settings, stats, sb, screen,
                                   snakeHead, snakes, snakeBody, food):
    """Check to see if the head of the snake bumpeed into food"""

    if pygame.sprite.spritecollideany(snakeHead, food):

        foodPart = pygame.sprite.spritecollideany(snakeHead, food)
        # Remermber food part is a food, we have to convert it to a snake part
        foodPart.remove(food)
        color = foodPart.color

        enlarge_snake(ai_settings, screen, stats, snakes, snakeBody, color)

        stats.score += 1
        sb.prep_score()

    check_high_score(stats, sb)

def check_snake_collisions(stats, snakeHead, snakes):
    snakeBody = snakes.copy()

    for snake in snakes:
        if snake.head or snake.head2:
            snakeBody.remove(snake)

    if pygame.sprite.spritecollideany(snakeHead, snakeBody):
        print("Happened")
        stats.game_active = False
        pygame.mouse.set_visible(True)

def update_screen(ai_settings, screen, sb, snake, food, snakeHead):
    """Update thescreen constantly"""

    # Redraw the screen during each loop. Make sure this is first
    screen.fill(ai_settings.black)

    # Draw the score
    sb.show_score()

    if sb.stats.score > 0 and not snakeHead.lock:
        snakeHead.lock = True


    # Draw the snake
    for snake_piece in snake.sprites():
        snake_piece.blitme()
        # if not snake_piece.head:
        for turnPoint in snake_piece.turnPoints:
            turnPoint.blitme()


    # Draw the snake food
    for snake_food in food.sprites():
        snake_food.blitme()

    # Make the most recently drawn screen visible
    pygame.display.flip() # Really need this for the screen to update

    # check_snakeHead_food_collisions

def check_high_score(stats, sb):
    """Check high score"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()