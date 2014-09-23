#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import equipment
from equipment import *
import battle
import gameresource
from util.tool import *
from monster_group import *
import gamestate


class Monster(attribute.Attribute):
    def __init__(self, mid):
        super(Monster, self).__init__()

        m_attribute = MC[mid].copy()

        self.level = gamestate.player.level + random.randint(m_attribute["level"][0], m_attribute["level"][1])

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
        gameresourceult = RandUtil.random([RandSeed(m["key"], m["val"]) for m in LMN[gamestate.SenceLevel]])
        gameresourceult = RandUtil.random([RandSeed(m["key"], m["val"]) for m in gameresourceult])

        for i in range(len(gameresourceult)):
            mid = gameresourceult[i]
            m = battle.BattleUnit(Monster(mid), gameresource.get_image("header"), [400, 20 + 160 * i], father, father.player)
            father.monsters.append(m)
            father.add(m)


