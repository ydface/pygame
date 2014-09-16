#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import math
import attribute
from attribute import *

Quality_White = 0
Quality_Greed = Quality_White + 1
Quality_Blue = Quality_Greed + 1
Quality_Purple = Quality_Blue + 1
Quality_Red = Quality_Purple + 1
Quality_Gold =  Quality_Red + 1

Equip_Hat = 0
Equip_Necklace = Equip_Hat + 1
Equip_Clothes = Equip_Necklace + 1
Equip_Left_Weapon = Equip_Clothes + 1
Equip_Right_Weapon = Equip_Left_Weapon + 1
Equip_Gaiter = Equip_Right_Weapon + 1
Equip_Shoes = Equip_Gaiter + 1
Equip_Left_Ring = Equip_Shoes + 1
Equip_Right_Ring = Equip_Left_Ring + 1
Equip_Talisman = Equip_Right_Ring + 1

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

