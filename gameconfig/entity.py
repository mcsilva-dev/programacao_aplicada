#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame


class Entity(ABC):
    def __init__(self, name: str, pos: tuple):
        self.name = name
        self.surf = pygame.image.load(f'./{name}')
        self.rect = self.surf.get_rect(left=pos[0], top=pos[1])
        self.speed = 0

    @abstractmethod
    def move(self, ):
        pass

