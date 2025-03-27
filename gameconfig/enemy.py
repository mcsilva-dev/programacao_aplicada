#!/usr/bin/python
# -*- coding: utf-8 -*-

from gameconfig.entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, pos: tuple):
        super().__init__(name, pos)

    def move(self, ):
        pass
