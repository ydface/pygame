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
    def __init__(self, mid):
        super(Monster, self).__init__()

        m_attribute = MC[mid].copy()

        self.level = random.randint(m_attribute["level"][0], m_attribute["level"][1])

        lv_addition = m_attribute["add"] * self.level
        rand_addition = random.randint(-10, 10)
        rand_addition = 1 + (rand_addition / 100.0)

        self.attribute = m_attribute["attr"]
        self.attribute = [attr * lv_addition * rand_addition for attr in self.attribute]
        self.name = m_attribute["name"]

        self.exp = int(m_attribute["exp"] * lv_addition)

        self.equip = None

        quality = RandUtil.random([RandSeed(m["key"], m["val"]) for m in m_attribute["equip"]])
        if quality is not None:
            eid = RandUtil.random([RandSeed(m["key"], m["val"]) for m in m_attribute["part"]])
            self.equip = equipment.Equipment.create_equipment(self.level, eid, quality, None)


    @staticmethod
    def create_monsters(father):
        result = RandUtil.random([RandSeed(m["key"], m["val"]) for m in LMN[gamestate.SenceLevel]])
        result = RandUtil.random([RandSeed(m["key"], m["val"]) for m in result])

        for i in range(len(result)):
            mid = result[i]
            m = battle.BattleUnit(Monster(mid), resource.getImage("header"), [400, 20 + 80 * i], father, father.player)
            father.monsters.append(m)
            father.add(m)


