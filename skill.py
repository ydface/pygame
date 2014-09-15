#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import pygame
from pygame.locals import *
import random
import mypygame
import label

skill_config = {
    "1": {
        "paras": [125, 25],
        "content": u"对当前目标造成(125 + 5 * 等级)% + 25点固定伤害",
        "cool_down": 0.0,
        "release_time": 1.0
    },
    "2": {
        "paras": [145, 25],
        "cool_down": 3,
        "release_time": 1.2
    },
    "3": {
        "paras": [100, 25, 30],
        "cool_down": 20,
        "release_time": 1.5
    },
    "4": {
        "paras": [100, 25, 30],
        "cool_down": 20,
        "release_time": 1.1
    },
    "5": {
        "paras": [175, 55],
        "cool_down": 35,
        "release_time": 1.8
    }
}

NORMAL = 1
CRIT = 2
MISS = 3

COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 128, 0)
COLOR_WHITE = (255, 255, 255)

screen = mypygame.screen


class SkillEffect(object):
    def __init__(self, skill, source, target, battle_inst):
        super(SkillEffect, self).__init__()

        self.skill = skill
        self.effect_paras = skill_config[str(self.skill.skill_id)]["paras"]
        self.source = source
        self.target = target
        self.btl_instance = battle_inst
        self.skill.go_cd(skill_config[str(self.skill.skill_id)]["cool_down"], skill_config[str(self.skill.skill_id)]["release_time"])

    def effect_value(self):
        return int(self.source.attack * (self.skill.level * 5 + self.effect_paras[0]) // 100 + self.effect_paras[1] - self.target.defense)

    def effect_active(self):
        if 1 == self.skill.skill_id or 5 == self.skill.skill_id:
            damage = self.effect_value()
            self.target.hp -= damage

            text = str(-damage)
            self.target.add_hp_change_label(text, 16, COLOR_RED)

        elif 3 == self.skill.skill_id or 4 == self.skill.skill_id:
            damage = self.effect_value()
            ra = random.randint(1, 100)
            text = str(-damage)
            if ra <= self.effect_paras[2]:
                damage = int(damage *1.5)
                text += u"暴击 "
            self.target.hp -= damage
            self.target.add_hp_change_label(text, 16, COLOR_RED)
        elif 2 == self.skill.skill_id:
            cure = self.effect_value()
            self.source.recover_hp(cure)

            text = "+" + str(cure)
            self.source.add_hp_change_label(text, 16, COLOR_GREEN)


class Skill(object):
    def __init__(self, skill_id, level):
        super(Skill, self).__init__()

        self.skill_id = skill_id
        self.level = level
        self.max_cool_down = 0.1
        self.cool_down = 0.1
        self.release_time = 1
        self.available = True

    def cd_update(self, **kwargs):
        time = kwargs['time']

        if self.cool_down > 0:
            self.cool_down -= time

        if self.cool_down <= 0 and self.release_time > 0:
            self.release_time -= time

        if self.release_time <= 0:
            self.available = True

    def go_cd(self, cd_time, release_time):
        self.available = False
        self.cool_down = cd_time
        self.max_cool_down = cd_time
        self.release_time = release_time

    def draw_process(self, father):
        #pygame.draw.rect(screen, (255, 255, 0), (father.rect[0] + 69, father.rect[1] + 54, 100, 4))
        #w = float(self.release_time) /self.max_cool_down
        #pygame.draw.rect(screen, (255, 0, 0), (father.rect[0] + 69, father.rect[1] + 54, w, 4))

        rect = Rect(father.rect[0] + 69 + 35, father.rect[1] + 48, 100, 4)
        view = label.LabelViewState(label.ViewForver)
        text = str(round(float(self.release_time), 2))
        text1 = label.FontLabel(rect, view, 12, text=text, father=self)
        text1.draw()

