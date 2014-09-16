#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import attribute
import save_data
import skill

level_exp_sequence = [100, 186, 368, 495, 602, 733, 901, 1186, 1423, 1765, 2132, 2598, 3065, 3656, 4645, 5243, 5923, 6885]
skill_study = {
    "4" : 3,
    "5" : 4,
    "6" : 5
}

class Player(attribute.Attribute):
    def __init__(self):
        super(Player, self).__init__()
        self.exp = 0
        self.n_exp = 0
        self.skills = []

        self.load_save()

    def load_save(self):
        user_obj = save_data.Save.load("user")
        self.level = user_obj["level"]
        self.exp = user_obj["exp"]
        self.n_exp = self.level_up_exp()
        self.hp = user_obj["hp"]
        self.max_hp = user_obj["max_hp"]
        self.speed1 = user_obj["speed1"]
        self.speed2 = user_obj["speed2"]
        self.attack = user_obj["attack"]
        self.defense = user_obj["defense"]
        self.hit = user_obj["hit"]
        self.dodge = user_obj["dodge"]
        self.crit = user_obj["crit"]
        self.crit_seal = user_obj["crit_seal"]
        self.wreck = user_obj["wreck"]
        self.parry = user_obj["parry"]

        skill_obj = save_data.Save.load("skill")
        for s in skill_obj:
            self.skills.append(skill.Skill(s["skill_id"], s["level"],self))

    def level_up_exp(self):
        global level_exp_sequence
        if self.level < len(level_exp_sequence):
            return level_exp_sequence[self.level]
        return 0

    def add_exp(self, exp):
        self.exp += exp
        if self.n_exp and self.exp >= self.n_exp:
            self.exp -= self.n_exp
            self.level += 1
            self.n_exp = self.level_up_exp()
            self.level_up_event()
        save_data.Save.save()

    def user_serialize_save(self):
        user_obj = dict()
        user_obj["level"] = self.level
        user_obj["exp"] = self.exp
        user_obj["hp"] = self.hp
        user_obj["speed1"] = self.speed1
        user_obj["speed2"] = self.speed2
        user_obj["attack"] = self.attack
        user_obj["defense"] = self.defense
        user_obj["hit"] = self.hit
        user_obj["dodge"] = self.dodge
        user_obj["crit"] = self.crit
        user_obj["crit_seal"] = self.crit_seal
        user_obj["wreck"] = self.wreck
        user_obj["parry"] = self.parry
        user_obj["max_hp"] = self.max_hp
        return user_obj

    def skill_serialize_save(self):
        skill_obj = []
        for s in self.skills:
            skill_obj.append({"skill_id": s.skill_id, "level": s.level})
        return skill_obj

    def level_up_event(self):
        global skill_study
        if skill_study.has_key(str(self.level)):
            self.skills.append(skill.Skill(skill_study[str(self.level)], 1))


