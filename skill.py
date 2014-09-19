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
import battle

SC = {
    1: {
        "paras": [1.25, 25],
        "effect": 1,
        "name": u"普通攻击",
        "content": u"对当前目标造成125% + (25 * 技能等级)点固定伤害",
        "cd": 0.0,
        "rt": 2.0,
        "anger": -8
    },
    2: {
        "paras": [1.45, 25, 0.2],
        "effect": 2,
        "name": u"对当前目标造成145% + (28 * 技能等级)点固定伤害, 技能额外增加20%暴击率",
        "cd": 15,
        "rt": 2.5,
        "anger": 25
    },
    3: {
        "paras": [1.15, 37, 0.35],
        "effect": 3,
        "name": u"对当前目标造成115% + (37 * 技能等级)点固定伤害, 技能额外增加35%暴击伤害",
        "cd": 20,
        "rt": 1.5,
        "anger": 20
    },
    4: {
        "paras": [1.20, 16, 0.15],
        "effect": 4,
        "name": u"对当前目标造成115% + (37 * 技能等级)点固定伤害, 并恢复造成伤害的15%血量",
        "cd": 30,
        "rt": 3,
        "anger": 20
    },
    5: {
        "paras": [1.75, 55, 0.1, 5],
        "effect": 5,
        "name": u"175% + (55 * 技能等级)点固定伤害, 并提升10%的伤害， 持续5秒",
        "cd": 35,
        "rt": 5,
        "anger": 35
    },
    6: {
        "paras": [0.9, 68, 1.5, 7],
        "effect": 6,
        "name": u"90% + (68 * 技能等级)点固定伤害, 附加每3秒造成一定伤害的持续伤害,持续7秒",
        "cd": 35,
        "rt": 6,
        "anger": 35
    },
    101: {
        "paras": [0.85, 10],
        "effect": 1,
        "name": u"普通攻击",
        "content": u"对当前目标造成(85 + 5 * 等级)% + 25点固定伤害",
        "cd": 0.0,
        "rt": 2.0,
        "anger": -3
    },
    102: {
        "paras": [1.00, 25],
        "effect": 1,
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

BTY_YUNXUAN = 1
BTY_SHANGHAI_INC = 2
BTY_SHANGHAI_DEC = 3
BTY_BAOJI_SEAL = 4
BTY_BAOJI_INC = 5
BTY_DOT = 6
BTY_HOT = 7
BTY_MINGZHONG_DEC = 8
BTY_ZUZHOU = 9
BTY_ABSORB_BLOOD = 10

screen = mypygame.screen


class SkillEffect(object):
    def __init__(self, skill, source, target):
        super(SkillEffect, self).__init__()

        self.skill = skill
        self.effect_paras = SC[self.skill.skill_id]["paras"]
        self.source = source
        self.target = target
        self.attack_ratio = self.effect_paras[0]
        self.fixed_damage = self.effect_paras[1] * self.skill.level
        self.damage = 0
        self.crit = 0
        self.hit = 0
        self.crit_damage = 0.0

        self.skill.go_cd()

    @staticmethod
    def create_skill_effect(skill, source, target):
        if skill.effect == 1:
            return SkillEffect_1(skill, source, target)
        elif skill.effect == 2:
            return SkillEffect_2(skill, source, target)
        elif skill.effect == 3:
            return  SkillEffect_3(skill, source, target)
        elif skill.effect == 4:
            return SkillEffect_4(skill, source, target)
        elif skill.effect == 5:
            return SkillEffect_5(skill, source, target)
        elif skill.effect == 6:
            return SkillEffect_6(skill, source, target)
        else:
            return SkillEffect(skill, source, target)
    #技能必命中?
    def hit_certainly(self):
        return False

    #被闪避?
    def source_miss(self):
        s_hit = self.source.unit.attribute_value(Attribute_Hit)
        t_dodge = self.target.unit.attribute_value(Attribute_Dodge)
        n = s_hit * 1.81
        m = s_hit * 1.04 + t_dodge * 0.96 + 0.01
        hit = max([n/m, 0.3])

        ra = random.randint(1, 100) / 100.0
        if ra >= hit:
            return True
        return False

    def effect_active(self):
        self.source.anger_change(self.skill.anger)
        if not self.hit_certainly() and self.source_miss():
            self.target.add_hp_change_label("MISS", 16, COLOR_WHITE)
            self.append_source_buff()
            self.append_target_buff()
        else:
            self.skill_damage()

    def skill_damage(self):
        s_atk = self.source.unit.attribute_value(Attribute_Attack)
        t_def = self.target.unit.attribute_value(Attribute_Defense)

        self.damage = max([(s_atk * 0.89 - t_def * 0.91) * self.attack_ratio, 1])
        damage_inc = self.source.buff_effect_value(BTY_SHANGHAI_INC)
        damage_dec = self.target.buff_effect_value(BTY_SHANGHAI_DEC)
        damage_rate = max([damage_inc - damage_dec, -0.7])
        self.damage *= 1 + damage_rate

        self.damage += self.fixed_damage
        self.ext_damage_calc()
        self.damage = int(self.damage)

        crit = self.crit_rate() + self.crit
        parry = self.parry_rate()

        text = str(-self.damage)
        ra = random.randint(1, 100) / 100.0
        if ra <= crit:
            self.damage *= (1.5 + self.crit_damage)
            self.damage = int(self.damage)
            text += u"暴击"
        elif ra > crit and ra <= parry:
            self.damage *= 0.5
            self.damage = int(self.damage)
            text += u"格挡"

        self.target.damaged(self.damage)
        self.target.add_hp_change_label(text, 16, COLOR_RED)

        self.source_absorb_blood()

        self.append_source_buff()
        if self.target.dead:
            return
        self.append_target_buff()

    def source_absorb_blood(self):
        pass

    def base_crit_rate(self):
        s_crit = self.source.unit.attribute_value(Attribute_Crit)
        t_crit_seal = self.target.unit.attribute_value(Attribute_Crit_Seal)
        n = s_crit * 0.83
        m = self.crit * 1.97 + t_crit_seal * 3.98 + 0.01
        crit = n / m
        return crit

    def base_parry_rate(self):
        s_wreck = self.source.unit.attribute_value(Attribute_Wreck)
        t_parry = self.target.unit.attribute_value(Attribute_Parry)
        n = t_parry * 0.83
        m = s_wreck * 1.97 + t_parry * 3.98 + 0.01
        parry = n / m
        return parry

    def crit_rate(self):
        crit = self.base_crit_rate()
        parry = self.base_parry_rate()
        crit = crit / (crit + parry + (1 - parry) * (1 - crit))
        return crit

    def parry_rate(self):
        crit = self.base_crit_rate()
        parry = self.base_parry_rate()
        parry = parry / (crit + parry + (1 - parry) * (1 - crit))
        return parry

    def ext_damage_calc(self):
        pass

    def append_source_buff(self):
        pass

    def append_target_buff(self):
        pass


class Skill(object):
    def __init__(self, skill_id, level, father):
        super(Skill, self).__init__()

        self.skill_id = skill_id
        self.level = level
        self.father = father
        self.available = False
        self.anger = SC[self.skill_id]["anger"]
        self.effect = SC[self.skill_id]["effect"]
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
        pygame.draw.rect(screen, COLOR_GREEN, (father.rect[0] + 69, father.rect[1] + 42, w, 4))

        text = str(round(float(self.release_time), 2))
        pos = [father.rect[0] + 69 + 35, father.rect[1] + 45]
        label.FontLabel.draw_label(12, text, COLOR_WHITE, pos)


class SkillEffect_1(SkillEffect):
    def __init__(self, skill, source, target):
        super(SkillEffect_1, self).__init__(skill, source, target)


class SkillEffect_2(SkillEffect):
    def __init__(self, skill, source, target):
        super(SkillEffect_2, self).__init__(skill, source, target)

        self.crit = self.effect_paras[2]


class SkillEffect_3(SkillEffect):
    def __init__(self, skill, source, target):
        super(SkillEffect_3, self).__init__(skill, source, target)

        self.crit_damage = self.effect_paras[2]


#吸收造成%c的伤害
class SkillEffect_4(SkillEffect):
    def __init__(self, skill, source, target):
        super(SkillEffect_4, self).__init__(skill, source, target)

        self.absorb = self.effect_paras[2]

    def source_absorb_blood(self):
        val = int(self.damage * self.absorb)
        self.source.recover_hp(val)
        self.source.add_hp_change_label(u"吸血 " + str(val), 16, COLOR_GREEN)


#增加%c的伤害
class SkillEffect_5(SkillEffect):
    def __init__(self, skill, source, target):
        super(SkillEffect_5, self).__init__(skill, source, target)

        self.para = self.effect_paras[2]
        self.round = self.effect_paras[3]

    def append_source_buff(self):
        battle.BattleBuff.append_buff(self.source, self.source, BTY_SHANGHAI_INC, self.round, self.para)


#使中毒
class SkillEffect_6(SkillEffect):
    def __init__(self, skill, source, target):
        super(SkillEffect_6, self).__init__(skill, source, target)

        self.round = self.effect_paras[3]
        self.interval = self.effect_paras[2]

    def append_source_buff(self):
        battle.BattleBuff.append_buff(self.source, self.target, BTY_DOT, self.round, int(self.damage/self.round), interval=self.interval)