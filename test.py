import random
from settings import Settings

settings = Settings()

for x in range(10):
    x_value = random.randint(0,settings.screen_width)
    y_value = random.randint(0,settings.screen_height)
    print(str(x_value) + "," + str(y_value))

for x in range(10):
    print(random.randint(0,10)) # This prints all the numbers from 0 to 10