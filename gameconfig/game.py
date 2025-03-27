#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from .menu import Menu
from .level import Level
from .configs import MENU_OPTION

class Game:
    def __init__(self, window: tuple = (600,480)) -> None:
        pygame.init()
        self.window = pygame.display.set_mode(size=window)
        self.run()

    def run(self) -> None:
        while True:
            menu = Menu(self.window)
            option = menu.run()
            match option:
                case 0:
                    level = Level(self.window, 'level 1')
                    level.run()
                case 1:
                    print('Score')
                case 2:
                    pygame.quit()
                    quit()
