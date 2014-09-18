#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import pygame
from pygame.locals import *
import random
import mypygame
import label
import attribute
import equipment

MC = {
    1: {
        "attr": [165, 165, 86, 23, 0.0, 0.0, 0, 0, 0, 0, 0],
        "lvadd": 0.2,
        "exp": 3
    },
    2: {
        "attr": [86, 86, 103, 15, 0.0, 0.0, 0, 0, 0, 0, 0],
        "lvadd": 0.3,
        "exp": 5
    },
    3: {
        "attr": [234, 234, 46, 41, 0.0, 0.0, 0, 0, 0, 0, 0],
        "lvadd": 0.2,
        "exp": 8
    },
    4: {
        "attr": [115, 115, 38, 69, 0.0, 0.0, 0, 0, 0, 0, 0],
        "lvadd": 1.2,
        "exp": 9
    },
    5: {
        "attr": [386, 386, 112, 95, 0.0, 0.0, 0, 0, 0, 0, 0],
        "lvadd": 0.2,
        "exp": 14
    }
}


class Monster(attribute.Attribute):
    def __init__(self, mid, level):
        super(Monster, self).__init__()

        self.level = level

        m_attribute = MC[mid]

        lv_addition = 1 + m_attribute["lvadd"] * level

        self.attribute = m_attribute["attr"]
        self.attribute = [attr * lv_addition for attr in self.attribute]

        self.exp = int(m_attribute["exp"] * lv_addition)

        self.equip = None
        ra = random.randint(0, 100)
        if ra < 15:
            eid = random.randint(1, 11)
            quality = random.randint(equipment.Quality_White, equipment.Quality_Gold)
            self.equip = equipment.Equipment.create_equipment(self.level, eid, quality)


