import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group
from turnPoint import TurnPoint

class Snake(Sprite):
    """A class to represent the snake"""

    def __init__(self, ai_settings, screen, stats):
        """Initialize thhe snake."""
        super(Snake, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect() # Screen's rectangle
        self.ai_settings = ai_settings
        self.stats = stats

        self.rect = pygame.Rect(self.ai_settings.screen_width/2,
                                self.ai_settings.screen_height/2,
                                ai_settings.snake_width, ai_settings.snake_height)
        self.center = self.rect.centerx
        self.y = self.rect.y

        # Testing these variables out
        self.color = self.ai_settings.jred

        self.length = self.stats.score

        self.head = False
        self.head2 = False
        self.lock = False
        self.end = False

        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

        # Create it's turn points
        self.turnPoints = Group()

    def blitme(self):
        """Draw the snake"""
        self.screen.fill(self.color, self.rect)

    def stop(self):
        self.moving_right = self.moving_left = self.moving_down = self.moving_up = False

    def update(self):
        """Update snake's position"""

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.snake_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.snake_speed_factor
        elif self.moving_up and self.rect.y > 0:
            self.y -= self.ai_settings.snake_speed_factor
        elif self.moving_down and self.rect.y < self. ai_settings.screen_height - 20:
            self.y += self.ai_settings.snake_speed_factor

        self.rect.centerx = self.center
        self.rect.y = self.y



    def direction(self):
        if self.moving_right:
            print("Right")
        elif self.moving_left:
            print("Left")
        elif self.moving_up:
            print("Up")
        elif self.moving_down:
            print("Down")
        else:
            print("Not moving")



    def updateBody(self):
        for x in range(0, self.length + 1):
            print(5)

