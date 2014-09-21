#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import pygame
import math
import resource
import attribute
from attribute import *
import random
from util.macro import *
import types
from equipment_template import *
import util.tool
from util.tool import *

DA = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

class Equipment(attribute.Attribute):
    def __init__(self):
        super(Equipment, self).__init__()
        self.template = 0

    @staticmethod
    def create_equipment(level, eid, quality, rand):
        if not eid in ETM:
            return None

        t_attr = ETM[eid]
        equip = Equipment()
        equip.level = level
        equip.template = eid
        equip.quality = quality
        equip.part = t_attr["part"]

        #print e_attr
        #品质对应的属性生成规则数据
        e_attr = t_attr["attr"].copy()
        b_attr = e_attr[equip.quality]
        #属性数量规则
        num_rand = b_attr["na"]
        #最终随机出的属性数量
        attr_num = RandUtil.random([RandSeed(m["k"], m["v"]) for m in num_rand])

        #属性类型列表
        attr_l = b_attr["attr_l"]
        #打乱顺序
        random.shuffle(attr_l)
        #获得属性
        r_attr_l = attr_l[0:attr_num]

        if "m_attr" in t_attr:
            m_attr = t_attr["m_attr"]
            r_attr_l.append(m_attr)

        equip.attribute = DA[:]
        for a in r_attr_l:
            rv = b_attr["attr_v"][a]
            equip.attribute[a] = random.randint(rv[0] * 100, rv[1] * 100) / 100.0

        addition = 1 + 0.4 * level
        equip.attribute = [equip.attribute[attr] * addition for attr in range(Attribute_Hp, Attribute_None)]

        equip.attribute[Attribute_Max_Hp] = equip.attribute[Attribute_Hp]

        if equip.part in RNAME:
            equip.image = resource.getImage(RNAME[equip.part] + str(equip.quality))
            equip.image = pygame.transform.scale(equip.image, (37, 37))
        else:
            equip.image = resource.getImage("item_" + str(equip.template))

        #equip.image = resource.getImage("item_" + str(equip.template))
        return equip

    @staticmethod
    def load_equipment( level, eid, quality, attr):
        if not eid in ETM:
            return None

        e_attr = ETM[eid]
        equip = Equipment()
        equip.level = level
        equip.template = eid
        equip.quality = quality
        equip.part = e_attr["part"]
        equip.attribute = attr
        if equip.part in RNAME:
            equip.image = resource.getImage(RNAME[equip.part] + str(equip.quality))
            equip.image = pygame.transform.scale(equip.image, (37, 37))
        else:
            equip.image = resource.getImage("item_" + str(equip.template))
        return equip

