#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

from gameconfig.background import Background
from gameconfig.configs import WIDTH, ENTITY_SPEED
from gameconfig.player import Player
from gameconfig.enemy import Enemy


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, path: str, position: tuple = (0, 0)) -> list[Background|Player|Enemy] | None:
        match entity_name:
            case 'level 1BG':
                bg_list = list()
                images = os.listdir(path)
                for speed, img in enumerate(sorted(images)):
                    bg_list.append(Background(f'{path}/{img}', position, ENTITY_SPEED.get(img)))
                    bg_list.append(Background(f'{path}/{img}', (WIDTH, 0), ENTITY_SPEED.get(img)))
                return bg_list
