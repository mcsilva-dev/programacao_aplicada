#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.font import Font
from pygame.surface import Surface
from pygame.rect import Rect
from .configs import (
    COLOR_RED,
    COLOR_WHITE,
    COLOR_YELLOW,
    MENU_OPTION,
    TITLE_FONT,
    TEXT_FONT
)


class Menu:
    def __init__(self, window: pygame.display) -> None:
        self.window = window
        self.surface = pygame.image.load('./assets/backgrounds/m1/main_menu.png')
        self.rect = self.surface.get_rect()
        self.menu_options = MENU_OPTION

    def run(self, ):
        position = 0
        pygame.mixer_music.load("./assets/sounds/main_menu.mp3")
        pygame.mixer_music.play(-1)
        while True:
            pygame.display.flip()
            self.window.blit(source=self.surface, dest=self.rect)
            self.menu_text(50, 'SPACE', TITLE_FONT, COLOR_RED, (576 / 2, 50))
            self.menu_text(50, 'SHIPS', TITLE_FONT,COLOR_RED, (576 / 2, 90))
    
            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if position < len(self.menu_options) - 1:
                            position += 1
                        else:
                            position = 0
                    if event.key == pygame.K_UP:
                        if position > 0:
                            position -= 1
                        else:
                            position = len(self.menu_options) - 1
                    if event.key == pygame.K_RETURN:
                        return position
                            
            for index, option in enumerate(self.menu_options):
                if index == position:
                    self.menu_text(30, option,TEXT_FONT, COLOR_YELLOW, (576 / 2, 180 + (30 * index)))
                else:
                    self.menu_text(30, option,TEXT_FONT, COLOR_WHITE, (576 / 2, 180 + (30 * index)))
                

    def menu_text(self, size: int, text: str, font: str, color: tuple, pos: tuple):
        text_font: Font = pygame.font.Font(font, size)
        text_surf: Surface = text_font.render(text, True, color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=pos)
        self.window.blit(source=text_surf, dest=text_rect)