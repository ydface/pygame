#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

skill_config = {
    "1": {
        "skill_effect": 1,
        "effect_paras": [125, 25]
    },
    "2":{
        "skill_effect": 2,
        "effect_paras": [145, 25]
    }
}


class SkillEffect(object):
    def __init__(self, skill_id, level):
        self.skill_id = skill_id
        self.skill_effect = skill_config[str(self.skill_id)]["skill_effect"]
        self.effect_paras = skill_config[str(self.skill_id)]["effect_paras"]
        self.level = level

    def effect_value(self, attack, defense):
        return int(attack * (self.level * 5 + self.effect_paras[0]) / float(100) + self.effect_paras[1] - defense)

    def effect_active(self, source):
        if 1 == self.skill_effect or 2 == self.skill_effect:
            damage = self.effect_value(source.attack, source.target.defense)
            source.target.hp -= damage
            return -damage
        elif 101 == self.skill_effect:
            cure = self.effect_value()
            source.hp += cure
            return cure


class Skill(object):
    def __init__(self, skill_id, level):
        self.skill_id = skill_id
        self.level = level
        self.cool_down = 0