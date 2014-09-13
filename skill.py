#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import random

skill_config = {
    "1": {
        "paras": [125, 25],
        "content": u"对当前目标造成(125 + 5 * 等级)% + 25点固定伤害",
        "cool_down": 15
    },
    "2": {
        "paras": [145, 25],
        "cool_down": 18
    },
    "3": {
        "paras": [100, 25, 30],
        "cool_down": 20
    }
}

NORMAL = 1
CRIT = 2
MISS = 3

COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 128, 0)
COLOR_WHITE = (255, 255, 255)


class SkillEffect(object):
    def __init__(self, skill, source, target, battle_inst):
        self.skill = skill
        self.effect_paras = skill_config[str(self.skill.skill_id)]["paras"]
        self.source = source
        self.target = target
        self.btl_instance = battle_inst
        self.skill.cool_down = skill_config[str(self.skill.skill_id)]["cool_down"]

    def effect_value(self):
        return int(self.source.attack * (self.skill.level * 5 + self.effect_paras[0]) // 100 + self.effect_paras[1] - self.target.defense)

    def effect_active(self):
        if 1 == self.skill.skill_id:
            damage = self.effect_value()
            self.target.hp -= damage

            text = str(-damage)
            self.btl_instance.add_hp_change_label(self.target, text, 16, COLOR_RED)
        elif 3 == self.skill.skill_id:
            damage = self.effect_value()
            ra = random.randint(1, 100)
            text = str(-damage)
            if ra <= self.effect_paras[2]:
                damage = int(damage *1.5)
                text += u"暴击 "
            self.target.hp -= damage
            self.btl_instance.add_hp_change_label(self.target, text, 16, COLOR_RED)
        elif 2 == self.skill.skill_id:
            cure = self.effect_value()
            self.source.recover_hp(cure)

            text = str(cure)
            self.btl_instance.add_hp_change_label(self.source, text, 16, COLOR_GREEN)


class Skill(object):
    def __init__(self, skill_id, level):
        self.skill_id = skill_id
        self.level = level
        self.cool_down = 0