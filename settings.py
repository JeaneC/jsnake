class Settings():
    """A class to store all settings for JSnake"""

    # Colors - This game will utilize 9 colors
    black = (0, 0, 0)
    jred = (204, 0, 0)
    jorange = (204, 102, 0)
    jyellow = (204, 204, 0)
    jgreen = (0, 204, 0)
    jcyan = (0, 204, 204)
    jblue = (0, 0, 204)
    jpurple = (102, 0, 204)
    jpink = (255, 0, 127)


    def __init__(self):

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800

        # Snake settings
        self.snake_width = 20
        self.snake_height = 20
        self.snake_speed_factor = 1

        # Snake Food settings
        self.snake_food_width = 15
        self.snake_food_height = 15



