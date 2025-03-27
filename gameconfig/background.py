#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import override

from gameconfig.configs import WIDTH
from gameconfig.entity import Entity


class Background(Entity):
    def __init__(self, name: str, pos: tuple, speed: int):
        super().__init__(name, pos)
        self.speed = speed

    @override
    def move(self):
        self.rect.centerx -= self.speed
        if self.rect.right <= 0:
            self.rect.left = WIDTH
