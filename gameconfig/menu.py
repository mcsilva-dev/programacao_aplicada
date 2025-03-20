#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.font import Font
from pygame.surface import Surface
from pygame.rect import Rect
import gameconfig.constants as constants

class Menu:
    def __init__(self, window: pygame.display) -> None:
        self.window = window
        self.surface = pygame.image.load('./assets/backgrounds/m1/main_menu.png')
        self.rect = self.surface.get_rect()

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load("./assets/sounds/main_menu.mp3")
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surface, dest=self.rect)
            self.menu_text(50, 'Space', constants.COLOR_RED, (constants.WIDTH / 2, 50))
            self.menu_text(50, 'Ships', constants.COLOR_RED, (constants.WIDTH / 2, 90))
            
            for i in range(len(constants.MENU_OPTIONS)):
                if i == menu_option:
                    self.menu_text(30, constants.MENU_OPTIONS[i], constants.COLOR_YELLOW, ((constants.WIDTH/2),200 + 30 * i))
                else:
                    self.menu_text(30, constants.MENU_OPTIONS[i], constants.COLOR_WHITE, ((constants.WIDTH/2),200 + 30 * i))
    
            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(constants.MENU_OPTIONS) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -=1
                        else:
                            menu_option = len(constants.MENU_OPTIONS) - 1
                    
                    
            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
