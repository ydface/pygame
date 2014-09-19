#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import math
import resource
import attribute
from attribute import *
import random
from util.macro import *


'''
Attribute_Name = ["血量", u"最大血量", u"攻击", u"防御", u"冷却加速", u"施法加速", u"命中",u"闪避", u"暴击", u"抗暴", u"破击", u"格挡"]
'''

equipment_template = {
    1: {
        "attr": [[121, 141], [121, 141], [0, 0], [1, 1], [1.2, 1.2], [0.8, 0.8], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        "lv_add": [0.2, 0.4, 0.7, 1.1, 1.6, 2.5],
        "part": Equip_Hat
    },
    2: {
        "attr": [[121, 141], [121, 141], [0, 0], [1, 1], [1.2, 1.2], [0.8, 0.8], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        "lv_add": [0.2, 0.4, 0.7, 1.1, 1.6, 2.5],
        "part": Equip_Clothes
    },
    3: {
        "attr": [[121, 141], [121, 141], [0, 0], [1, 1], [1.2, 1.2], [0.8, 0.8], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        "lv_add": [0.2, 0.4, 0.7, 1.1, 1.6, 2.5],
        "part": Equip_Necklace
    },
    4: {
        "attr": [[121, 141], [121, 141], [0, 0], [1, 1], [1.2, 1.2], [0.8, 0.8], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        "lv_add": [0.2, 0.4, 0.7, 1.1, 1.6, 2.5],
        "part": Equip_Left_Weapon
    },
    5: {
        "attr": [[121, 141], [121, 141], [0, 0], [1, 1], [1.2, 1.2], [0.8, 0.8], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        "lv_add": [0.2, 0.4, 0.7, 1.1, 1.6, 2.5],
        "part": Equip_Right_Weapon
    },
    6: {
        "attr": [[121, 141], [121, 141], [0, 0], [1, 1], [1.2, 1.2], [0.8, 0.8], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        "lv_add": [0.2, 0.4, 0.7, 1.1, 1.6, 2.5],
        "part": Equip_Left_Ring
    },
    7: {
        "attr": [[121, 141], [121, 141], [0, 0], [1, 1], [1.2, 1.2], [0.8, 0.8], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        "lv_add": [0.2, 0.4, 0.7, 1.1, 1.6, 2.5],
        "part": Equip_Right_Ring
    },
    8: {
        "attr": [[121, 141], [121, 141], [0, 0], [1, 1], [1.2, 1.2], [0.8, 0.8], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        "lv_add": [0.2, 0.4, 0.7, 1.1, 1.6, 2.5],
        "part": Equip_Gaiter
    },
    9: {
        "attr": [[121, 141], [121, 141], [0, 0], [1, 1], [1.2, 1.2], [0.8, 0.8], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        "lv_add": [0.2, 0.4, 0.7, 1.1, 1.6, 2.5],
        "part": Equip_Shoes
    },
    10: {
        "attr": [[121, 141], [121, 141], [0, 0], [1, 1], [1.2, 1.2], [0.8, 0.8], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        "lv_add": [0.2, 0.4, 0.7, 1.1, 1.6, 2.5],
        "part": Equip_Talisman
    },
    11: {
        "attr": [[121, 141], [121, 141], [0, 0], [1, 1], [1.2, 1.2], [0.8, 0.8], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        "lv_add": [0.2, 0.4, 0.7, 1.1, 1.6, 2.5],
        "part": Equip_Belt
    },
}


class Equipment(attribute.Attribute):
    def __init__(self):
        super(Equipment, self).__init__()
        self.template = 0

    @staticmethod
    def create_equipment(level, eid, quality, rand):
        if not equipment_template.has_key(eid):
            return None

        e_attr = equipment_template[eid]
        equip = Equipment()
        equip.level = level
        equip.template = eid
        equip.quality = quality
        equip.part = e_attr["part"]
        equip.random = rand

        addition = 1 + e_attr["lv_add"][quality] * level

        equip.attribute = e_attr["attr"]
        attribute_min = [int(equip.attribute[attr][0] * addition) for attr in range(Attribute_Hp, Attribute_None)]
        attribute_max = [int(equip.attribute[attr][1] * addition) for attr in range(Attribute_Hp, Attribute_None)]

        if equip.random is None:
            equip.random = random.randint(1, 100) / 100.0
        equip.attribute = [attribute_min[attr] + equip.random * (attribute_max[attr] - attribute_min[attr]) for attr in range(Attribute_Hp, Attribute_None)]

        equip.image = resource.getImage("item_" + str(equip.template))
        return equip

