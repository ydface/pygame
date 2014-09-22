#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import attribute
import save_data
import skill
import equipment
from attribute import *
import math

LES = [80, 561, 1536, 3014, 5011, 7547, 10640, 14300, 18576, 23466, 28997, 35201, 42100, 49723, 58097, 67253, 77221, \
       88034, 99723, 112324, 125874, 140409, 155964, 172584, 190310, 209179, 229239, 250534, 273114, 297026, 322320, \
       349043, 377260, 407017, 438376, 471390, 506130, 542653, 581021, 621303, 663579, 707907, 754363, 803020, 853977, \
       907291, 963057, 1021341, 1082281, 1145917, 1212367, 1281726, 1354070, 1429563, 1508257, 1590274, 1675706, \
       1764746, 1857440, 1953934, 2054314, 2158831, 2267494, 2380503, 2497943, 2620077, 2746963, 2878771, 3015629, \
       3157834, 3305429, 3458623, 3617537, 3782560, 3953680, 4131166, 4315200, 4505937, 4703817, 4908840, 5121303, \
       5341291, 5569440, 5805646, 6050229, 6303394, 6565760, 6837189, 7118160, 7408777, 7709806, 8021063, 8343143, \
       8675966, 9020686, 9376914, 9745211, 10125829, 10519680, 10926606, 11347109, 11781714, 13759226, 14281534, \
       14820686, 15377709, 15952577, 16547117, 17160660, 17794131, 18447891, 19123560, 19820674, 20540263, 21282377]
SS = {
    4: 3,
    5: 4,
    6: 5,
    7: 6
}

AttrAdd = [37, 37, 6, 4, 2, 1, 0, 0, 0, 0, 0, 0]
InitAttr = [378, 378, 126, 63, 0, 0, 50, 27, 34, 29, 18, 18]


class Player(attribute.Attribute):
    def __init__(self):
        super(Player, self).__init__()
        self.exp = 0
        self.n_exp = 0
        self.skills = []
        self.equips = []
        self.e_equips = []

        self.load_save()

    def load_save(self):
        user_obj = save_data.Save.load("user")
        self.level = user_obj["level"]
        self.exp = user_obj["exp"]
        self.n_exp = self.level_up_exp()

        self.attribute = [InitAttr[attr] + self.level * AttrAdd[attr] for attr in range(Attribute_Hp, Attribute_None)]

        skill_obj = save_data.Save.load("skill")
        for s in skill_obj:
            self.skills.append(skill.Skill(s["skill_id"], s["level"], self))

        item_obj = save_data.Save.load("item")
        for i in item_obj:
            if i is None:
                self.equips.append(None)
            else:
                equip = equipment.Equipment.load_equipment(i["level"], i["eid"], i["quality"], i["attr"], i.get("skill", 0))
                if equip.skill_id:
                    equip.skill = skill.Skill(equip.skill_id, 1, self)
                self.equips.append(equip)


        equiped_obj = save_data.Save.load("equiped")
        for i in range(len(equiped_obj)):
            if equiped_obj[i] is None:
                self.e_equips.append(None)
            else:
                equip = equipment.Equipment.load_equipment(equiped_obj[i]["level"], equiped_obj[i]["eid"], equiped_obj[i]["quality"], equiped_obj[i]["attr"], equiped_obj[i].get("skill", 0))
                if equip.skill_id:
                    equip.skill = skill.Skill(equip.skill_id, 1, self)
                self.attribute = [self.attribute[attr] + equip.attribute[attr] for attr in range(Attribute_Hp, Attribute_None)]
                self.e_equips.append(equip)

    def level_up_exp(self):
        global LES
        if self.level < len(LES):
            return LES[self.level]
        return 0

    def add_exp(self, exp):
        self.exp += exp
        if self.n_exp and self.exp >= self.n_exp:
            self.exp -= self.n_exp
            self.level += 1
            self.n_exp = self.level_up_exp()
            self.level_up_event()
        save_data.Save.save()

    def get_equipment(self, equip):
        if equip is not None:
            max_idx = len(self.equips) - 1
            for idx in range(0, max_idx):
                if self.equips[idx] is None:
                    self.equips[idx] = equip
                    save_data.Save.save()
                    return

    def destory_equipment(self, equip):
        self.equips.remove(equip)
        self.equips.append(None)

    def user_serialize_save(self):
        user_obj = dict()
        user_obj["level"] = self.level
        user_obj["exp"] = self.exp
        return user_obj

    def skill_serialize_save(self):
        skill_obj = []
        for s in self.skills:
            skill_obj.append({"skill_id": s.skill_id, "level": s.level})
        return skill_obj

    def item_serialize_save(self):
        item_obj = []
        for e in self.equips:
            if e is None:
                item_obj.append(e)
            else:
                item_obj.append({"eid": e.template, "level": e.level, "quality": e.quality, "attr": e.attribute, "skill": e.skill_id})
        return item_obj

    def equiped_serialize_save(self):
        equiped_obj = []
        for e in self.e_equips:
            if e is None:
                equiped_obj.append(e)
            else:
                equiped_obj.append({"eid": e.template, "level": e.level, "quality": e.quality, "attr": e.attribute, "skill": e.skill_id})
        return equiped_obj

    def level_up_event(self):
        global SS
        if SS.has_key(self.level):
            self.skills.append(skill.Skill(SS[self.level], 1, self))

        self.attribute = [self.attribute[attr] + AttrAdd[attr] for attr in range(Attribute_Hp, Attribute_None)]

    def put_on_equipment(self, idx):
        if idx >= len(self.equips) or self.equips[idx] is None:
            return

        equip = self.equips[idx]
        self.equips[idx] = None

        part = equip.part
        if self.e_equips[part] is not None:
            o_equip = self.e_equips[part]
            if o_equip.skill is not None:
                self.skills.remove(o_equip.skill)
            self.attribute = [self.attribute[attr] - o_equip.attribute[attr] for attr in range(Attribute_Hp, Attribute_None)]
            self.equips[idx] = o_equip
        self.e_equips[part] = equip
        self.attribute = [self.attribute[attr] + equip.attribute[attr] for attr in range(Attribute_Hp, Attribute_None)]

        if equip.skill is not None:
            self.skills.append(equip.skill)
    def put_off_equipment(self, equip):
        if equip.skill is not None:
            self.skills.remove(equip.skill)
        self.attribute = [self.attribute[attr] - equip.attribute[attr] for attr in range(Attribute_Hp, Attribute_None)]
        self.e_equips[equip.part] = None
        self.get_equipment(equip)
        pass

    def part_equipment(self, part):
        if part >= len(self.e_equips):
            self.e_equips.extend([None] * (part - len(self.e_equips) + 1))
        return self.e_equips[part]
