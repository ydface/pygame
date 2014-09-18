#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import pygame
from pygame.locals import *
import random
import mypygame
import label
import math
from attribute import *
from util.color import *

SC = {
    1: {
        "paras": [125, 25],
        "name": u"普通攻击",
        "content": u"对当前目标造成(125 + 5 * 等级)% + 25点固定伤害",
        "cd": 0.0,
        "rt": 2.0,
        "anger": -8
    },
    2: {
        "paras": [145, 25],
        "name": u"普通攻击",
        "cd": 3,
        "rt": 2.5,
        "anger": 25
    },
    3: {
        "paras": [100, 25, 30],
        "name": u"普通攻击",
        "cd": 20,
        "rt": 1.5,
        "anger": 20
    },
    4: {
        "paras": [100, 25, 30],
        "name": u"普通攻击",
        "cd": 30,
        "rt": 3,
        "anger": 20
    },
    5: {
        "paras": [175, 55],
        "name": u"普通攻击",
        "cd": 35,
        "rt": 5,
        "anger": 35
    },
    101: {
        "paras": [85, 10],
        "name": u"普通攻击",
        "content": u"对当前目标造成(85 + 5 * 等级)% + 25点固定伤害",
        "cd": 0.0,
        "rt": 2.0,
        "anger": -3
    },
    102: {
        "paras": [100, 25],
        "name": u"普通攻击",
        "content": u"对当前目标造成(100 + 5 * 等级)% + 25点固定伤害",
        "cd": 3.0,
        "rt": 2.0,
        "anger": 14
    },
}

NORMAL = 1
CRIT = 2
MISS = 3

screen = mypygame.screen


class SkillEffect(object):
    def __init__(self, skill, source, target):
        super(SkillEffect, self).__init__()

        self.skill = skill
        self.effect_paras = SC[self.skill.skill_id]["paras"]
        self.source = source
        self.target = target
        self.skill.go_cd()

    def effect_value(self):
        s_atk = self.source.unit.attribute_value(Attribute_Attack)
        t_def = self.target.unit.attribute_value(Attribute_Defense)

        return max([1, int(s_atk * (self.skill.level * 5 + self.effect_paras[0]) // 100 + self.effect_paras[1] - t_def)])

    def effect_active(self):
        self.source.anger_change(self.skill.anger)
        if self.skill.skill_id in [1, 5, 101, 102]:
            damage = self.effect_value()
            self.target.damaged(damage)
            text = str(-damage)
            self.target.add_hp_change_label(text, 16, COLOR_RED)

        elif 3 == self.skill.skill_id or 4 == self.skill.skill_id:
            damage = self.effect_value()
            ra = random.randint(1, 100)
            text = str(-damage)
            if ra <= self.effect_paras[2]:
                damage = int(damage * 1.5)
                text += u"暴击 "
            self.target.damaged(damage)

            self.target.add_hp_change_label(text, 16, COLOR_RED)
        elif 2 == self.skill.skill_id:
            cure = self.effect_value()
            self.source.recover_hp(cure)

            text = "+" + str(cure)
            self.source.add_hp_change_label(text, 16, COLOR_GREEN)


class Skill(object):
    def __init__(self, skill_id, level, father):
        super(Skill, self).__init__()

        self.skill_id = skill_id
        self.level = level
        self.father = father
        self.available = False
        self.anger = SC[self.skill_id]["anger"]
        self.init_cd(SC[self.skill_id]["cd"], SC[self.skill_id]["rt"])

    def cd_update(self, **kwargs):
        time = kwargs['time']

        if self.cool_down > 0:
            self.cool_down -= time

    def release_update(self, **kwargs):
        time = kwargs['time']
        if self.release_time > 0:
            self.release_time -= time
        if self.release_time <= 0:
            self.available = True

    def init_cd(self, cd_time, release_time):
        q1 = math.exp(self.father.level % 3) * self.level
        q2 = math.exp(self.father.level * 1.1)
        q = q1 * q2

        cdr = round(q / (self.father.attribute_value(Attribute_Speed1) + 0.01), 4)
        cdr = min([max([0.5, cdr]), 1.0])
        cd_time *= cdr
        self.cool_down = cd_time
        self.max_cool_down = cd_time

        rtr = round(q / (self.father.attribute_value(Attribute_Speed2) + 0.01), 4)
        rtr = min([max([0.5, rtr]), 1.0])
        release_time *= rtr
        self.release_time = release_time
        self.max_release_time = release_time

    def go_cd(self):
        self.available = False
        self.cool_down = self.max_cool_down
        self.release_time = self.max_release_time

    def draw_process(self, father):
        w = 71 - float(self.release_time) * 71 / self.max_release_time
        pygame.draw.rect(screen, COLOR_GREEN, (father.rect[0] + 69, father.rect[1] + 45, w, 4))

        text = str(round(float(self.release_time), 2))
        pos = [father.rect[0] + 69 + 35, father.rect[1] + 48]
        label.FontLabel.draw_label(12, text, COLOR_WHITE, pos)

