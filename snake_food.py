import pygame
import random
from pygame.sprite import Sprite

class SnakeFood(Sprite):
    """To create a snake food block particle in the game"""

    def __init__(self, ai_settings, screen, stats, snake):
        """Initialize snake food stuff"""
        super(SnakeFood, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()  # Screen's rectangle
        self.stats = stats

        # This will be problematic later in the rare scenario the food
        # Spawns in the snake's mouth
        self.x_value = random.randint(0, ai_settings.screen_width - 20)
        self.y_value = random.randint(0, ai_settings.screen_height - 20)

        self.rect = pygame.Rect(self.x_value, self.y_value,
                                ai_settings.snake_food_width,
                                ai_settings.snake_food_height)
        self.center = float(self.rect.centerx)
        self.y = float(self.rect.y)

        self.randomNumber = random.randint(0, 7)
        # print(self.randomNumber)
        self.color = self.chooseColor(self.randomNumber)
        # print(self.color)

    def blitme(self):
        """Draw the snake food at a random location"""
        self.screen.fill(self.color, self.rect)

    def chooseColor(self, randomNumber):
        if randomNumber == 0:
            return self.ai_settings.jred
        elif randomNumber == 1:
            return self.ai_settings.jorange
        elif randomNumber == 2:
            return self.ai_settings.jyellow
        elif randomNumber == 3:
            return self.ai_settings.jgreen
        elif randomNumber == 4:
            return self.ai_settings.jcyan
        elif randomNumber == 5:
            return self.ai_settings.jblue
        elif randomNumber == 6:
            return self.ai_settings.jpurple
        elif randomNumber == 7:
            return self.ai_settings.jpink
