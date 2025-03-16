#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.font import Font
from pygame.surface import Surface
from pygame.rect import Rect


class Menu:
    def __init__(self, window: pygame.display) -> None:
        self.window = window
        self.surface = pygame.image.load('./assets/backgrounds/m1/main_menu.png')
        self.rect = self.surface.get_rect()

    def run(self, ):
        pygame.mixer_music.load("./assets/sounds/main_menu.mp3")
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surface, dest=self.rect)
            self.menu_text(50, 'Space', (255, 0, 0), (576 / 2, 50))
            self.menu_text(50, 'Ships', (255, 0, 0), (576 / 2, 90))
            self.menu_text(30, 'Start Game', (255, 255, 255), (576 / 2, 180))
            self.menu_text(30, 'Score', (255, 255, 255), (576 / 2, 210))
            self.menu_text(30, 'Exit', (255, 255, 255), (576 / 2, 240))

            pygame.display.flip()
            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)