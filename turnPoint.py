import pygame
from pygame.sprite import Sprite


class TurnPoint(Sprite):

    def __init__(self, ai_settings, screen, movePointX, movePointY, direction):
        """Create a turnpoint object at the snake head's current position"""
        super(TurnPoint, self).__init__()
        #Super inherits all stuff from sprie

        self.screen = screen
        self.ai_settings = ai_settings
        self.rect = pygame.Rect(movePointX, movePointY, 1, 1)
        self.right = self.left = self.up = self.down = False
        self.center = movePointX
        self.y = movePointY

        if(direction == 1):
            self.right = True
        elif(direction == 2):
            self.left = True
        elif(direction == 3):
            self.down = True
        elif(direction == 4 ):
            self.up = True

    def blitme(self):
        """Draw the turn point"""
        self.screen.fill(self.ai_settings.black, self.rect) #Change this to a color to see turn points