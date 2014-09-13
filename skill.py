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
        self.skill_effect = skill_config[str(self.skill_id)]
        self.level = level

    def damage_value(self):
        return self.level * 5 + self.skill_effect["effect_paras"][0] + self.skill_effect["effect_paras"][1]


class Skill(object):
    def __init__(self, skill_id, level):
        self.skill_id = skill_id
        self.level = level
        self.cool_down = 0