import os

WIDTH = 576
HEIGHT = 324

#Colors
COLOR_RED = (255, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)

TITLE_FONT = 'assets/font/GreenStrand-8Vzz.ttf'
TEXT_FONT = 'assets/font/RocketRinder-yV5d.ttf'

ENTITY_SPEED = {img: speed+1 for speed, img in enumerate(sorted(os.listdir('assets/backgrounds/m2'), reverse=True))}

MENU_OPTION = [
    'Start Game',
    'Score',
    'Exit'
]