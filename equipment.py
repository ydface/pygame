#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import math
import resource
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
Equip_Left_Ring = Equip_Right_Weapon + 1
Equip_Right_Ring = Equip_Left_Ring + 1
Equip_Gaiter = Equip_Right_Ring + 1
Equip_Shoes = Equip_Gaiter + 1
Equip_Talisman = Equip_Right_Ring + 1

Equip_Name = [u"头盔", u"项链", u"护甲", u"主手", u"副手", u"左手戒指", u"右手戒指", u"护腿", u"鞋子", u"护符"]
QName = [u"粗糙", u"精致", u"无暇", u"完美", u"神器", u"传奇"]

equipment_template = {
    1: {
        "attr": [121, 121, 7, 2, 1.2, 0.8, 0, 0, 0, 0, 0, 0],
        "lv_add": [0.2, 0.4, 0.7, 1.1, 1.6, 2.5],
        "part": Equip_Hat
    },
    2: {
        "attr": [264, 264, 3, 1, 0.3, 0.2, 0, 0, 0, 0, 0, 0],
        "lv_add": [0.2, 0.4, 0.7, 1.1, 1.6, 2.5],
        "part": Equip_Clothes
    },
    3: {
        "attr": [34, 34, 18, 2, 1.2, 0.8, 0, 0, 0, 0, 0, 0],
        "lv_add": [0.2, 0.4, 0.7, 1.1, 1.6, 2.5],
        "part": Equip_Necklace
    },
    4: {
        "attr": [3, 3, 18, 2, 1.2, 0.8, 4, 0, 0, 0, 0, 0],
        "lv_add": [0.2, 0.4, 0.7, 1.1, 1.6, 2.5],
        "part": Equip_Left_Weapon
    },
    5: {
        "attr": [34, 34, 18, 2, 1.2, 0.8, 0, 0, 0, 0, 0, 0],
        "lv_add": [0.2, 0.4, 0.7, 1.1, 1.6, 2.5],
        "part": Equip_Right_Weapon
    },
    6: {
        "attr": [34, 34, 18, 2, 1.2, 0.8, 0, 0, 0, 0, 0, 0],
        "lv_add": [0.2, 0.4, 0.7, 1.1, 1.6, 2.5],
        "part": Equip_Left_Weapon
    },
    7: {
        "attr": [34, 34, 18, 2, 1.2, 0.8, 0, 0, 0, 0, 0, 0],
        "lv_add": [0.2, 0.4, 0.7, 1.1, 1.6, 2.5],
        "part": Equip_Right_Ring
    },
    8: {
        "attr": [34, 34, 18, 2, 1.2, 0.8, 0, 0, 0, 0, 0, 0],
        "lv_add": [0.2, 0.4, 0.7, 1.1, 1.6, 2.5],
        "part": Equip_Gaiter
    },
    9: {
        "attr": [34, 34, 18, 2, 1.2, 0.8, 0, 0, 0, 0, 0, 0],
        "lv_add": [0.2, 0.4, 0.7, 1.1, 1.6, 2.5],
        "part": Equip_Shoes
    },
    10: {
        "attr": [34, 34, 18, 2, 1.2, 0.8, 0, 0, 0, 0, 0, 0],
        "lv_add": [0.2, 0.4, 0.7, 1.1, 1.6, 2.5],
        "part": Equip_Talisman
    },
}


class Equipment(attribute.Attribute):
    def __init__(self):
        super(Equipment, self).__init__()
        self.template = 0

    @staticmethod
    def create_equipment(level, eid, quality):
        if not equipment_template.has_key(eid):
            return None

        e_attr = equipment_template[eid]
        equip = Equipment()
        equip.level = level
        equip.template = eid
        equip.quality = quality
        equip.part = e_attr["part"]

        addition = 1 + e_attr["lv_add"][quality] * level

        equip.attribute = e_attr["attr"]
        equip.attribute = [equip.attribute[attr] * addition for attr in range(Attribute_Hp, Attribute_None)]

        equip.image = resource.getImage("item_" + str(equip.template))
        return equip

