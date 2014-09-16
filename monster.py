#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import pygame
from pygame.locals import *
import random
import mypygame
import label
import attribute

a = [378, 378, 126, 63, 0, 0, 50, 27, 34, 29, 18, 18]
monster_config = {
    "1": {
        "attribute": [165, 165, 86, 23, 0.0, 0.0, 0, 0, 0, 0, 0],
        "lvadd": 1.2,
        "exp": 3
    },
    "2": {
        "attribute": [86, 86, 103, 15, 0.0, 0.0, 0, 0, 0, 0, 0],
        "lvadd": 1.3,
        "exp": 5
    },
    "3": {
        "attribute": [234, 234, 46, 41, 0.0, 0.0, 0, 0, 0, 0, 0],
        "lvadd": 1.2,
        "exp": 8
    },
    "4": {
        "attribute": [115, 115, 38, 69, 0.0, 0.0, 0, 0, 0, 0, 0],
        "lvadd": 1.2,
        "exp": 9
    },
    "5": {
        "attribute": [386, 386, 112, 95, 0.0, 0.0, 0, 0, 0, 0, 0],
        "lvadd": 1.2,
        "exp": 14
    }
}


class Monster(attribute.Attribute):
    def __init__(self, mid, level):
        super(Monster, self).__init__()

        self.level = level

        m_attribute = monster_config[str(mid)]

        lv_addition = m_attribute["lvadd"] * level

        self.attribute = m_attribute["attribute"]
        self.attribute = [attr * lv_addition for attr in self.attribute]

        self.exp = int(m_attribute["exp"] * lv_addition)


