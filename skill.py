#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import pygame
import random
import mypygame
import label
from util.color import *
from util.macro import *
import battle
import res

SC = {
    1: {
        "paras": [0.85, 25, 0.15],
        "effect": 1,
        "name": u"野球拳",
        "content": u"造成(85 + 5 * 技能等级)% + 25点固定伤害，同时有15%的概率打断目标施法",
        "cd": 0.0,
        "rt": 1.2,
        "anger": -5,
        "res": 1
    },
    2: {
        "paras": [1.45, 28, 0.2],
        "effect": 2,
        "name": u"傲剑狂刀",
        "content": u"造成(145 + 5 * 技能等级)% + 28点固定伤害, 技能额外增加20%暴击率",
        "cd": 5,
        "rt": 2.5,
        "anger": 6,
        "res": 2
    },
    3: {
        "paras": [1.25, 37, 0.35],
        "effect": 3,
        "name": u"力劈华山",
        "content": u"造成(125 + 5 * 技能等级) + 37点固定伤害, 技能额外增加35%暴击伤害",
        "cd": 7,
        "rt": 1.5,
        "anger": 7,
        "res": 3
    },
    4: {
        "paras": [1.20, 16, 0.45],
        "effect": 4,
        "name": u"吸星大法",
        "content": u"造成(120 + 5 * 技能等级) + 16点固定伤害, 并恢复造成伤害的45%血量",
        "cd": 15,
        "rt": 3,
        "anger": 0,
        "res": 4
    },
    5: {
        "paras": [1.75, 55, 0.1, 5],
        "effect": 5,
        "name": u"易筋经",
        "content": u"造成(175 + 5 * 技能等级) + 55点固定伤害, 并提升10%的伤害， 持续5秒",
        "cd": 21,
        "rt": 4,
        "anger": 0,
        "res": 5
    },
    6: {
        "paras": [0.9, 68, 1, 7],
        "effect": 6,
        "name": u"生死符",
        "content": u"造成(90 + 5 * 技能等级) + 68点固定伤害, 附加每1秒造成一定伤害的持续伤害,持续7秒",
        "cd": 24,
        "rt": 4,
        "anger": 0,
        "res": 6
    },
    7: {
        "paras": [0.2, 0],
        "effect": 7,
        "name": u"回春术(低级)",
        "content": u"恢复当前最大生命值60%的生命值",
        "cd": 25,
        "rt": 2,
        "anger": 0,
        "res": 7
    },
    8: {
        "paras": [0.4, 0],
        "effect": 7,
        "name": u"回春术(中级)",
        "content": u"恢复当前最大生命值60%的生命值",
        "cd": 25,
        "rt": 2,
        "anger": 0,
        "res": 7
    },
    9: {
        "paras": [0.6, 0],
        "effect": 7,
        "name": u"回春术(高级)",
        "content": u"恢复当前最大生命值60%的生命值",
        "cd": 25,
        "rt": 2,
        "anger": 0,
        "res": 7
    },
    10: {
        "paras": [0.05, 0],
        "effect": 8,
        "name": u"奥义·闪",
        "content": u"5%几率秒杀对手",
        "cd": 25,
        "rt": 0.3,
        "anger": 0,
        "res": 8
    },
    101: {
        "paras": [0.85, 10],
        "effect": 0,
        "name": u"火球",
        "content": u"造成(85 + 5 * 等级)% + 25点固定伤害",
        "cd": 0.0,
        "rt": 2.0,
        "anger": -3,
        "res": 1
    },
    102: {
        "paras": [1.00, 25],
        "effect": 0,
        "name": u"火焰突击",
        "content": u"造成(100 + 5 * 等级)% + 25点固定伤害",
        "cd": 3.0,
        "rt": 2.0,
        "anger": 14,
        "res": 2
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
        self.attack_ratio = self.effect_paras[0] + 0.05 * self.skill.level
        self.fixed_damage = self.effect_paras[1]
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
            return SkillEffect_3(skill, source, target)
        elif skill.effect == 4:
            return SkillEffect_4(skill, source, target)
        elif skill.effect == 5:
            return SkillEffect_5(skill, source, target)
        elif skill.effect == 6:
            return SkillEffect_6(skill, source, target)
        elif skill.effect == 7:
            return SkillEffect_7(skill, source, target)
        elif skill.effect == 8:
            return SkillEffect_8(skill, source, target)
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

        ra = random.randint(1, int((crit + parry) * 100) + 30) / 100.0
        #print ra, crit, parry
        if ra <= crit:
            self.damage *= (1.5 + self.crit_damage)
            self.damage = int(self.damage)
            self.target.damaged(self.damage)
            text = str(-self.damage) + u"暴击"
            self.target.add_hp_change_label(text, 20, COLOR_PURPLE)
        elif ra > crit and ra <= parry:
            self.damage *= 0.5
            self.damage = int(self.damage)
            self.target.damaged(self.damage)
            text = str(-self.damage) + u"格挡"
            self.target.add_hp_change_label(text, 20, COLOR_WHITE)
        else:
            self.target.damaged(self.damage)
            text = str(-self.damage)
            self.target.add_hp_change_label(text, 16, COLOR_RED)

        self.source_absorb_blood()

        self.append_source_buff()
        if self.target.dead:
            return
        self.append_target_buff()
        self.interrupt_release()

    def interrupt_release(self):
        pass

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
        return min([crit, 1.0])

    def parry_rate(self):
        crit = self.base_crit_rate()
        parry = self.base_parry_rate()
        parry = parry / (crit + parry + (1 - parry) * (1 - crit))
        return min([parry, 1.0])

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
        self.name = SC[self.skill_id]["name"]
        self.anger = SC[self.skill_id]["anger"]
        self.effect = SC[self.skill_id]["effect"]
        self.init_cd(SC[self.skill_id]["cd"], SC[self.skill_id]["rt"])
        res_id = SC[self.skill_id]["res"]
        self.image = res.get_image("skill_" + str(res_id))

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
        cdr = 1 - ((self.level - 1) * 0.05)
        cd_time *= cdr
        self.cool_down = cd_time
        self.max_cool_down = cd_time

        release_time *= cdr
        self.release_time = release_time
        self.max_release_time = release_time

    def go_cd(self):
        self.available = False
        self.cool_down = self.max_cool_down
        self.release_time = self.max_release_time

    def draw_process(self, father):
        w = 71 - float(self.release_time) * 71 / self.max_release_time
        pygame.draw.rect(screen, COLOR_GREEN, (father.rect[0] + 69, father.rect[1] + 42, w, 4))

        text = self.name + "(" + str(round(float(self.release_time), 2)) + ")"
        pos = [father.rect[0] + 69 + 35, father.rect[1] + 45]
        label.FontLabel.draw_label(12, text, COLOR_WHITE, pos)


class SkillEffect_1(SkillEffect):
    def __init__(self, skill, source, target):
        super(SkillEffect_1, self).__init__(skill, source, target)

        self.interrupt_rate = self.effect_paras[2]

    def interrupt_release(self):
        ra = random.randint(1, 100) / 100.0
        if ra <= self.interrupt_rate:
            self.target.next_skill.release_time = self.target.next_skill.max_release_time
            self.target.add_hp_change_label(u"打断", 20, COLOR_RED)


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
        self.source.add_hp_change_label(u"伤害↑", 20, COLOR_GOLD)
        #label.FontLabel.draw_label(12, , COLOR_GOLD, [self.target.rect[0] + 5, self.target.rect[1] - 5])


#使中毒
class SkillEffect_6(SkillEffect):
    def __init__(self, skill, source, target):
        super(SkillEffect_6, self).__init__(skill, source, target)

        self.round = self.effect_paras[3]
        self.interval = self.effect_paras[2]

    def append_source_buff(self):
        battle.BattleBuff.append_buff(self.source, self.target, BTY_DOT, self.round, int(self.damage/self.round), interval=self.interval)


#回春术
class SkillEffect_7(SkillEffect):
    def __init__(self, skill, source, target):
        super(SkillEffect_7, self).__init__(skill, source, target)

        self.prec = self.effect_paras[0]

    def effect_active(self):
        self.source.anger_change(self.skill.anger)
        hp_val = int(self.source.unit.attribute_value(Attribute_Max_Hp) * self.prec)
        self.source.recover_hp(hp_val)
        self.source.add_hp_change_label(u"回春 " + str(hp_val), 16, COLOR_GREEN)


#奥义·闪
class SkillEffect_8(SkillEffect):
    def __init__(self, skill, source, target):
        super(SkillEffect_8, self).__init__(skill, source, target)

        self.rate = self.effect_paras[0]

    def effect_active(self):
        self.source.anger_change(self.skill.anger)
        ra = random.randint(1, 100) / 100.0
        if ra <= self.rate:
            damage = self.target.unit.attribute_value(Attribute_Hp)
            self.target.damaged(damage)
            self.source.add_hp_change_label(u"必杀 " + str(damage), 16, COLOR_PURPLE)