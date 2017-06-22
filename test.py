from testObject import testObject
from snake import Snake
from pygame.sprite import Group



# Prototype Snake
snakeHead = testObject()
bodyOne = testObject()
bodyTwo = testObject()

# Group of the snake parts
testGroup = Group()
testGroup.add(snakeHead)  # Add the head as the first element
testGroup.add(bodyOne)
testGroup.add(bodyTwo)

print(testGroup.sprites())
