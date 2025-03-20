#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from .menu import Menu

class Game:
    def __init__(self, window: tuple = (600,480)) -> None:
        pygame.init()
        self.window = pygame.display.set_mode(size=window)
        self.run()

    def run(self) -> None:
        while True:
            menu = Menu(self.window)
            menu_option = menu.run()
            match menu_option:
                case 0:
                    print("Play")
                case 1:
                    print("Options")
                case 2:
                    pygame.quit()
                    quit()
            