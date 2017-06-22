class GameStats():
    """Track statistics for JSnake"""

    def __init__(self, ai_settings):
        """Initialize sttatistics"""
        self.ai_settings = ai_settings
        self.reset_stats()


        self.game_active = True # Currently game auto runs

        self.high_score = 0

    def reset_stats(self):
        """Stats that reset on game start"""
        self.score = 0
        