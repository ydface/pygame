#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import pygame
import pygame.mixer
from pygame.locals import *
import mypygame
import game_ui.mission_ui
import random
import resource
import label
import util.node
import gamestate
import button
import skill
import monster
import player
from attribute import *
from util.color import *

screen = mypygame.screen


class ExitButton(button.Button):
    def __init__(self, father):
        pos = [345, 500]
        image1 = resource.getImage("start_normal")
        image0 = resource.getImage("start_down")

        super(ExitButton, self).__init__(pos, image1, image0, father)

    def click_up_effect(self):
        gamestate.current_ui = game_ui.mission_ui.UIGame()


class BattleBuff(util.node.Node):
    def __init__(self, source, target, effect, round, para, **kwargs):
        super(BattleBuff, self).__init__()

        self.source = source
        self.target = target
        self.effect = effect
        self.round = round
        self.para = para
        self.interval = kwargs.get("interval", 0)   #生效间隔
        self.content = kwargs.get("content", u"无描述")
        self.time = self.interval  #生效剩余时间
        self.image = resource.getImage("skill_" + str(self.effect))
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 2, self.image.get_height() // 2))
        self.rect = self.image.get_rect()
        self.detail = None

    def draw(self, index):
        self.rect.topleft = (self.target.rect[0], self.target.rect[1] + self.target.rect[3] + 5)
        screen.blit(self.image, self.rect)
        label.FontLabel.draw_label(12, str(round(self.round, 1)), COLOR_WHITE, (self.rect[0], self.rect[1] + 15))

    def update(self, **kwargs):
        time = kwargs["time"]
        self.round -= time
        if self.round <= 0:
            self.target.buffs.remove(self)
            return
        if self.interval:
            self.time -= time
            if self.time <= 0:
                self.time = self.interval
                #buff效果
                if self.effect == skill.BTY_HOT:
                    self.target.recover(self.para)
                    text = u"持续 " + str(self.para)
                    self.target.add_hp_change_label(text, 16, COLOR_GREEN)
                elif self.effect == skill.BTY_DOT:
                    self.target.damaged(self.para)
                    text = u"中毒" + str(-self.para)
                    self.target.add_hp_change_label(text, 16, COLOR_RED)

    @staticmethod
    def append_buff(source, target, effect, round, para, **kwargs):
        target.buffs.append(BattleBuff(source, target, effect, round, para, **kwargs))


class BattleUnit(button.Button):
    def __init__(self, unit, image, pos, father, target, **kwargs):
        super(BattleUnit, self).__init__(pos, image, resource.getImage("header"), father)
        self.unit = unit
        self.dead = False
        self.father = father
        self.target = target
        self.skills = kwargs.get('skill', [skill.Skill(101, 1, self.unit), skill.Skill(102, 1, self.unit)])
        self.next_skill = self.skills[0]
        self.recover_time = 0.1
        self.anger = 0
        self.buffs = []

    def draw(self):
        screen.blit(self.image, (self.rect[0], self.rect[1]))
        if isinstance(self.unit, monster.Monster):
            label.FontLabel.draw_label(12, self.unit.name, COLOR_WHITE, (self.rect[0] + 80, self.rect[1] + 1))
        #绘制等级
        text = str(self.unit.level)
        label.FontLabel.draw_label(12, text, COLOR_WHITE, (self.rect[0] + 60, self.rect[1] + 3))

        #绘制血条
        hp_label = int(float(self.unit.attribute_value(Attribute_Hp)) / self.unit.attribute_value(Attribute_Max_Hp) * 100)
        if hp_label:
            pygame.draw.rect(screen, COLOR_RED, (self.rect[0] + 69, self.rect[1] + 22, hp_label, 8))

        text = str(self.unit.attribute_value(Attribute_Hp)) + " / " + str(self.unit.attribute_value(Attribute_Max_Hp))
        label.FontLabel.draw_label(8, text, COLOR_WHITE, (self.rect[0] + 71, self.rect[1] + 20))

        ##绘制怒气条
        anger_label = int(float(self.anger) / 100 * 100)
        if anger_label:
            pygame.draw.rect(screen, COLOR_BLUE, (self.rect[0] + 69, self.rect[1] + 31, anger_label, 8))
        text = str(self.anger) + " / " + str(100)
        label.FontLabel.draw_label(8, text, COLOR_WHITE, (self.rect[0] + 83, self.rect[1] + 30))

        if not self.dead:
            self.next_skill.draw_process(self)
        else:
            if isinstance(self.unit, player.Player):
                pass
        for child in self.child:
            child.draw()

        index = 0
        for buff in self.buffs:
            buff.draw(index)
            index += 1

    def click_up_effect(self):
        if self in self.father.monsters and not self.dead:
            self.target.target = self

    def update(self, **kwargs):
        time = kwargs['time']

        if not self.dead and not self.father.end:
            for s in self.skills:
                s.cd_update(**kwargs)
            self.next_skill.release_update(**kwargs)
        if self.father.end:
            self.recover(time)

        for child in self.child:
            child.update(**kwargs)

        for buff in self.buffs:
            buff.update(**kwargs)

    def recover(self, time):
        self.recover_time -= time
        if self.recover_time <= 0:
            self.recover_time = 0.1
            hpr = self.unit.attribute_value(Attribute_Max_Hp) / 30
            if self.unit.hp_inc(hpr):
                self.dead = False
                self.target = None

                for s in self.skills:
                    s.release_time = s.max_release_time
                self.father.new_battle()

    def damaged(self, damage):
        if self.unit.hp_dec(damage):
            self.dead = True

    def anger_change(self, val):
        self.anger -= val
        self.anger = min([max([self.anger, 0]), 100])

    def recover_hp(self, val):
        self.unit.hp_inc(val)

    def active(self):
        if self.dead:
            return
        if not self.target or self.target.dead:
            for m in self.father.monsters:
                if not m.dead:
                    self.target = m

        if self.next_skill.available:
            effect = skill.SkillEffect.create_skill_effect(self.next_skill, self, self.target)
            effect.effect_active()
            self.skill_available()

        if self.target.unit.attribute_value(Attribute_Hp) == 0:
            self.target.dead = True
            if isinstance(self.target.unit, monster.Monster):
                gamestate.player.add_exp(self.target.unit.exp)
                gamestate.player.get_equipment(self.target.unit.equip)

                view = label.LabelViewState(label.ViewTimer, 0.6, [0, -0.4])
                rect = [self.rect[0] + 13, self.rect[1] - 3]
                lb = label.FontLabel(rect, view, 12, text="exp " + str(self.target.unit.exp), color=label.COLOR_GREEN, father=self)
                self.add(lb)

    def add_hp_change_label(self, text, font_size, color):
        view = label.LabelViewState(label.ViewTimer, 1, [0, -1])
        rect = [self.rect[0] + 200, self.rect[1] + 30]
        lb = label.FontLabel(rect, view, font_size, text=text, color=color, father=self)
        self.add(lb)

    def skill_available(self):
        self.next_skill = self.skills[0]
        mlen = len(self.skills) - 1
        while mlen >= 0:
            sk = self.skills[mlen]
            mlen -= 1
            if self.anger < sk.anger:
                continue
            if sk.cool_down <= 0:
                self.next_skill = sk
                print "next ", sk.skill_id
                break

    def buff_effect_value(self, effect):
        val = 0
        for buff in self.buffs:
            if buff.effect == effect:
               val += buff.para
        return val


class Battle(util.node.Node):
    def __init__(self, level):
        super(Battle, self).__init__()

        self.end = True
        self.player = BattleUnit(gamestate.player, resource.getImage("header"), [100, 360], self, None, skill=gamestate.player.skills)
        self.player.dead = True
        self.add(self.player)
        self.monsters = []

        self.next_delay = random.randint(3, 5)
        self.add(ExitButton(self))

    def update(self, **kwargs):
        time = kwargs['time']
        self.player.update(**kwargs)
        if not self.end:
            self.player.active()

            if not self.check_end():
                for monster in self.monsters:
                    if monster.dead:
                        continue
                    monster.update(**kwargs)
                    monster.active()
                    if self.check_end():
                        break
            for child in self.child:
                child.update(**kwargs)

    def new_battle(self):
        self.end = False
        self.player.dead = False
        monster.Monster.create_monsters(self)

    def check_end(self):
        if self.end:
            return self.end

        if self.player.unit.attribute_value(Attribute_Hp) == 0:
            self.end = True
            for m in self.monsters:
                self.remove(m)
            self.monsters = []
        else:
            for m in self.monsters:
                if not m.dead:
                    return False
            self.end = True

            for m in self.monsters:
                self.remove(m)
            self.monsters = []
        return self.end

