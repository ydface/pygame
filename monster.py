#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import pygame
from pygame.locals import *
import random
import mypygame
import gamestate
import label
import attribute
import equipment
from equipment import *
import battle
import resource

MC = {
    1: {
        "attr": [75, 75, 86, 23, 0.0, 0.0, 0, 0, 0, 0, 0, 0],
        "lvadd": 0.6,
        "exp": 3
    },
    2: {
        "attr": [43, 43, 103, 15, 0.0, 0.0, 0, 0, 0, 0, 0, 0],
        "lvadd": 0.9,
        "exp": 5
    },
    3: {
        "attr": [115, 115, 46, 41, 0.0, 0.0, 0, 0, 0, 0, 0, 0],
        "lvadd": 1.3,
        "exp": 8
    },
    4: {
        "attr": [42, 42, 38, 69, 0.0, 0.0, 0, 0, 0, 0, 0, 0],
        "lvadd": 1.7,
        "exp": 9
    },
    5: {
        "attr": [386, 386, 112, 95, 0.0, 0.0, 0, 0, 0, 0, 0, 0],
        "lvadd": 2.4,
        "exp": 14
    }
}

MGROUP_1_1 = {
    9: [1, 1, 2],
    8: [1, 2, 2],
    9: [1, 2, 3],
    9: [2, 2, 3],
    8: [2, 3, 4],
    8: [2, 3, 5],
    8: [2, 3, 4, 5],
    8: [3, 4, 5],
    12: [2, 2, 2],
    13: [1, 1, 1],
}

MGROUP_1_2 = {
    9: [1, 1, 2],
    8: [1, 2, 2],
    9: [1, 2, 3],
    9: [2, 2, 3],
    8: [2, 3, 4],
    8: [2, 3, 5],
    8: [2, 3, 4, 5],
    8: [3, 4, 5],
    12: [2, 2, 2],
    13: [1, 1, 1],
}

MGROUP_1_3 = {
    9: [1, 1, 2],
    8: [1, 2, 2],
    9: [1, 2, 3],
    9: [2, 2, 3],
    8: [2, 3, 4],
    8: [2, 3, 5],
    8: [2, 3, 4, 5],
    8: [3, 4, 5],
    12: [2, 2, 2],
    13: [1, 1, 1],
}

MN = {
    60: MGROUP_1_1,
    30: MGROUP_1_2,
    10: MGROUP_1_3
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
            self.equip = equipment.Equipment.create_equipment(self.level, eid, quality, None)


    @staticmethod
    def create_monsters(father):
        num = random.randint(1, 100)
        for i in range(len(MN)):
            ra = MN[i]
            if i > 0:
                ra = MN[i] + MN[i-1]
            if num < ra:
                num = 3 + i
                break
        num = min([num, 5])
        for i in range(0, num):
            level = random.randint(max([1, gamestate.player.level - 3]), gamestate.player.level)
            mid = random.randint(1, 5)
            m = battle.BattleUnit(Monster(mid, level), resource.getImage("header"), [400, 20 + 80 * i], father, father.player)
            father.monsters.append(m)
            father.add(m)


