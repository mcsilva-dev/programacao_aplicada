#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.display

from gameconfig.entity import Entity
from gameconfig.entityFactory import EntityFactory


class Level:
    def __init__(self, window: pygame.display.set_mode, name: str) -> None:
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = list()
        self.entity_list.extend(EntityFactory.get_entity('level 1BG', "assets/backgrounds/m2"))

    def run(self):
        while True:
            for entity in self.entity_list:
                self.window.blit(source=entity.surf, dest=entity.rect)
                entity.move()
            pygame.display.flip()
