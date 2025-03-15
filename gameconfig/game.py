#!/usr/bin/python
# -*- coding: utf-8 -*-
from pygame import init, display
from .menu import Menu

class Game:
    def __init__(self, window: tuple = (600,480)) -> None:
        init()
        self.window = display.set_mode(size=window)
        self.run()

    def run(self) -> None:
        while True:
            menu = Menu(self.window)
            menu.run()
            # Check for all events
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit()
            #         break
