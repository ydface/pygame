#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import math
import attribute
from attribute import *

Quality_White = 0
Quality_Greed = 1
Quality_Blue = 2
Quality_Purple = 3
Quality_Red = 4
Quality_Gold = 5
Quality_None = 6

Equip_Hat = 0
Equip_Necklace = 1
Equip_Clothes = 2
Equip_Left_Weapon = 3
Equip_Right_Weapon = 4
Equip_Gaiter = 5
Equip_Shoes = 6
Equip_Left_Ring = 7
Equip_Right_Ring = 8
Equip_Talisman = 9

equipment_template = {
    "1": {
        "attribute": [121, 121, 7, 2, 1.2, 0.8, 0, 0, 0, 0, 0, 0],
        "lv_add": [0.2, 0.4, 0.7, 1.1, 1.6, 2.5],
        "part": Equip_Hat
    },
    "2": {
        "attribute": [264, 264, 3, 1, 0.3, 0.2, 0, 0, 0, 0, 0, 0],
        "lv_add": [0.2, 0.4, 0.7, 1.1, 1.6, 2.5],
        "part": Equip_Clothes
    },
    "3": {
        "attribute": [34, 34, 18, 2, 1.2, 0.8, 0, 0, 0, 0, 0, 0],
        "lv_add": [0.2, 0.4, 0.7, 1.1, 1.6, 2.5],
        "part": Equip_Left_Weapon
    },
}


class Equipment(attribute.Attribute):
    def __init__(self):
        super(Equipment, self).__init__()
        self.template = 0

    @staticmethod
    def create_equipment(level, eid, quality):
        if not equipment_template.has_key(str(eid)):
            return None

        e_attr = equipment_template[str(eid)]
        equip = Equipment()
        equip.level = level
        equip.template = eid
        equip.quality = quality
        equip.part = e_attr["part"]

        addition = 1 + e_attr["lv_add"][quality] * level

        equip.attribute = e_attr["attribute"]
        equip.attribute = [equip.attribute[attr] * addition for attr in range(Attribute_Hp, Attribute_None)]

        return equip

