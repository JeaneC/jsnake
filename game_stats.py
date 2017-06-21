class GameStats():
    """Track statistics for JSnake"""

    def __init__(self, ai_settings):
        """Initialize sttatistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = True # Currentely game auto runs

    def reset_stats(self):
        """Stats that reset on game start"""
        self.score = 0
        