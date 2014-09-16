#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import pygame
from pygame.locals import *
import random
import mypygame
import label
import attribute

monster_config = {
    "1": {
        "hp": 165,
        "attack": 86,
        "defense": 23,
        "speed1": 0.0,
        "speed2": 0.0,
        "lvadd": 1.2,
        "exp": 3
    },
    "2": {
        "hp": 86,
        "attack": 103,
        "defense": 15,
        "speed1": 0.0,
        "speed2": 0.0,
        "lvadd": 1.3,
        "exp": 5
    },
    "3": {
        "hp": 234,
        "attack": 46,
        "defense": 41,
        "speed1": 0.0,
        "speed2": 0.0,
        "lvadd": 1.2,
        "exp": 8
    },
    "4": {
        "hp": 115,
        "attack": 38,
        "defense": 69,
        "speed1": 0.0,
        "speed2": 0.0,
        "lvadd": 1.2,
        "exp": 9
    },
    "5": {
        "hp": 386,
        "attack": 112,
        "defense": 95,
        "speed1": 0.0,
        "speed2": 0.0,
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
        self.hp = int(m_attribute["hp"] * lv_addition)
        self.max_hp = self.hp
        self.attack = m_attribute["attack"] * lv_addition
        self.defense = m_attribute["defense"] * lv_addition
        self.speed1 = m_attribute["speed1"] * lv_addition
        self.speed2 = m_attribute["speed2"] * lv_addition
        self.exp = int(m_attribute["exp"] * lv_addition)


