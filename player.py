#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import attribute
import save_data
import skill
import equipment
from attribute import *

LES = [100, 186, 368, 495, 602, 733, 901, 1186, 1423, 1765, 2132, 2598, 3065, 3656, 4645, 5243, 5923, 6885]
SS = {
    4: 3,
    5: 4,
    6: 5,
    16: 6
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
            self.skills.append(skill.Skill(s["skill_id"], s["level"],self))

        item_obj = save_data.Save.load("item")
        for i in item_obj:
            if i is None:
                self.equips.append(None)
            else:
                self.equips.append(equipment.Equipment.load_equipment(i["level"], i["eid"], i["quality"], i["attr"]))

        equiped_obj = save_data.Save.load("equiped")
        for i in range(len(equiped_obj)):
            if equiped_obj[i] is None:
                self.e_equips.append(None)
            else:
                equip = equipment.Equipment.load_equipment(equiped_obj[i]["level"], equiped_obj[i]["eid"], equiped_obj[i]["quality"], equiped_obj[i]["attr"])
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
                item_obj.append({"eid": e.template, "level": e.level, "quality": e.quality, "attr": e.attribute})
        return item_obj

    def equiped_serialize_save(self):
        equiped_obj = []
        for e in self.e_equips:
            if e is None:
                equiped_obj.append(e)
            else:
                equiped_obj.append({"eid": e.template, "level": e.level, "quality": e.quality, "attr": e.attribute})
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
            self.attribute = [self.attribute[attr] - o_equip.attribute[attr] for attr in range(Attribute_Hp, Attribute_None)]
            self.equips[idx] = o_equip
        self.e_equips[part] = equip
        self.attribute = [self.attribute[attr] + equip.attribute[attr] for attr in range(Attribute_Hp, Attribute_None)]

    def part_equipment(self, part):
        return self.e_equips[part]
