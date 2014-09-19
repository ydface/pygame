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
import util.tool
from util.tool import *
from monster_group import *


class Monster(attribute.Attribute):
    def __init__(self, mid, level):
        super(Monster, self).__init__()

        self.level = level

        m_attribute = MC[mid]

        lv_addition = m_attribute["add"] * level

        self.attribute = m_attribute["attr"]
        self.attribute = [attr * lv_addition for attr in self.attribute]

        self.exp = int(m_attribute["exp"] * lv_addition)

        self.equip = None

        quality = RandUtil.random([RandSeed(m["key"], m["val"]) for m in m_attribute["equip"]])
        if quality is not None:
            eid = random.randint(1, 11)
            #quality = random.randint(equipment.Quality_White, equipment.Quality_Gold)
            self.equip = equipment.Equipment.create_equipment(self.level, eid, quality, None)


    @staticmethod
    def create_monsters(father):
        result = RandUtil.random([RandSeed(m["key"], m["val"]) for m in LMN[gamestate.SenceLevel]])
        result = RandUtil.random([RandSeed(m["key"], m["val"]) for m in result])

        for i in range(len(result)):
            level = random.randint(max([1, gamestate.player.level - 3]), gamestate.player.level)
            mid = result[i]
            m = battle.BattleUnit(Monster(mid, level), resource.getImage("header"), [400, 20 + 80 * i], father, father.player)
            father.monsters.append(m)
            father.add(m)


