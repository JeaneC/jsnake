import pygame.ftfont

class Scoreboard():
    """A class for scoring"""

    def __init__(self, ai_settings, screen, stats):
        self.screen = screen

        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48, bold=True)

        # Prepare the initial score image
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        """Turn the score into a rendered image."""
        score_str = "{:,}".format(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_settings.black)

        # Displace the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        high_score_str = "{:,}".format(self.stats.high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color,
                                                 self.ai_settings.black)

        # Displace the score at the top right of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        """Draw score"""
        self.screen.blit(self.score_image, self.score_rect)
       ## self.screen.blit(self.high_score_image, self.high_score_rect) Disable high score