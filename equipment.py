#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import pygame
import res
import attribute
from equipment_template import *
from util.tool import *
import skill
import gamestate

DA = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

class Equipment(attribute.Attribute):
    def __init__(self):
        super(Equipment, self).__init__()
        self.template = 0
        self.attribute = DA[:]
        self.skill_id = 0
        self.skill_level = 0
        self.skill = None

    def get_save(self):
        save = dict()
        save["eid"] = self.template
        save["level"] = self.level
        save["quality"] = self.quality
        save["attr"] = self.attribute
        if self.skill:
            save["skill"] = {"id": self.skill_id, "lv": self.skill_level}
        else:
            save["skill"] = None
        return save

    @staticmethod
    def create_equipment(level, eid, quality, rand):
        if not eid in ETM:
            return None

        t_attr = ETM[eid].copy()
        equip = Equipment()
        equip.level = level
        equip.template = eid
        equip.quality = quality
        equip.part = t_attr["part"]

        #print e_attr
        #品质对应的属性生成规则数据
        if "attr" in t_attr:
            e_attr = t_attr["attr"]
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

            for a in r_attr_l:
                rv = b_attr["attr_v"][a]
                equip.attribute[a] = random.randint(rv[0] * 100, rv[1] * 100) / 100.0

            addition = 1 + 0.4 * level
            equip.attribute = [equip.attribute[attr] * addition for attr in range(Attribute_Hp, Attribute_None)]

            equip.attribute[Attribute_Max_Hp] = equip.attribute[Attribute_Hp]

        if "skill" in t_attr:
            rs = t_attr["skill"]
            rs = rs[equip.quality]
            rsk = RandUtil.random([RandSeed(m["k"], m["v"]) for m in rs])
            if rsk:
                equip.skill_id = rsk["id"]
                equip.skill_level = rsk["lv"]
                equip.skill = skill.Skill(equip.skill_id, equip.skill_level, gamestate.player)
            #print equip.part

        if equip.part in RNAME:
            equip.image = res.get_image(RNAME[equip.part] + str(equip.quality))
            equip.image = pygame.transform.scale(equip.image, (37, 37))
        else:
            equip.image = res.get_image("item_" + str(equip.template))

        #equip.image = resource.get_image("item_" + str(equip.template))
        return equip

    @staticmethod
    def load_equipment(level, eid, quality, attr, sk):
        if not eid in ETM:
            return None

        e_attr = ETM[eid]
        equip = Equipment()
        equip.level = level
        equip.template = eid
        equip.quality = quality
        equip.part = e_attr["part"]
        equip.attribute = attr
        if sk:
            equip.skill_id = sk["id"]
            equip.skill_level = sk["lv"]

        if equip.part in RNAME:
            equip.image = res.get_image(RNAME[equip.part] + str(equip.quality))
            equip.image = pygame.transform.scale(equip.image, (37, 37))
        else:
            equip.image = res.get_image("item_" + str(equip.template))
        return equip

